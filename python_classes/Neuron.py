import random
from copy import copy
from collections import Counter
import sys

# Nombre maximal possible
MAX_DIST = 3

BASE_WEIGHT = 10
RECOMPENSE = 8

class NeuronNetwork:
    def __init__(self, maxDist, nbSticks):
        # Enregistrement des neurons
        self.neurons = []
        for i in range(1, nbSticks + 1):
            self.neurons.append(Neuron(self, i))
        # Création des connexions avec poid par défaut
        for neuron in self.neurons:
            neuron.makeConnections(maxDist, nbSticks, BASE_WEIGHT)
        self.initPath()

    # Renvoie le neuron d'index index
    # Renvoie None si index est invalide
    def getNeuron(self, index):
        if index - 1 >= 0 and index <= len(self.neurons):
            return self.neurons[index - 1]
        else:
            return None

    # Historique de la partie
    def initPath(self):
        self.path = {}

    # Ajout d'une connexion dans l'historique
    def activateNeuronPath(self, neuron1, neuron2):
        self.path[neuron1] = neuron2

    # Récompense des connexions établies durant la partie
    # Effet de bord: réinitialisation de l'historique
    def recompenseConnections(self):
        for neuron1,neuron2 in self.path.items():
            neuron1.recompenseConnection(neuron2)
        self.initPath()

    #Classe à surcharger si nous voulons punir les connexions
    def punisConnections(self):
        pass

    #Agrège tous les neurons du réseau de neuron
    def agregAllNeurons(self, netw2):
        for neuron in self.neurons:
            for neuron2 in netw2.neurons:
                if (neuron.index == neuron2.index):
                    neuron.agregNeuron(neuron2)

    # Affiche les connexions
    def printAllConnections(self):
        for neuron in self.neurons: neuron.printConnections()

    # Affiche les scores de chaque neurons
    def printScores(self):
        scores = {}
        for neuron in self.neurons:
            for n,s in neuron.connections.items():
                if n not in scores:
                    scores[n] = s
                else:
                    scores[n] = scores[n] + s
        for neuron, score in scores.items():
            print(neuron.asString(), score)


class Neuron:
    def __init__(self, network, index):
        # Réseau dans lequel est contenu le Neuron
        self.network = network
        # Correspond au nombre de baton restant
        self.index = index
        # Liaison vers d'autre neuron avec un indice de poid.
        # Map<Neuron, int>
        self.connections = {}

    # Crée les connexions initiales
    def makeConnections(self, maxDist, nbSticks, baseWeight):
        if self.index != nbSticks:
            nb = maxDist * 2 + 1
        else:
            nb = maxDist + 1
        for i in range(1, nb):
            neuron = self.network.getNeuron(self.index - i)
            # Si le neuron existe on crée une connexion
            if neuron != None:
                self.connections[neuron] = baseWeight

    # Choisi le neuron à jouer avec la méthode weighted_choice
    # Le neuron doit être atteignable (vérifié par testNeuron)
    # Condition d'arret:
    # 0 <= len(connectionsClone) <= len(connections)
    def chooseConnectedNeuron(self, shift):
        connectionsClone = copy(self.connections)
        neuron = self.weighted_choice(connectionsClone)
        while (len(connectionsClone) > 0 and not neuron.testNeuron(self.index-shift)):
            connectionsClone.pop(neuron)
            neuron = self.weighted_choice(connectionsClone)
        return neuron

    # renvoie un booléen: True si la différence entre la 'inValue' et la valeur
    # du neurone actuel est comprise entre 1 et 3 inclus
    def testNeuron(self, inValue):
        dif = inValue - self.index
        return dif >= 1 and dif <= 3

    # Ajoute une récompense au poids de la connexion avec un neuron donné
    def recompenseConnection(self, neuron):
        self.connections[neuron] += RECOMPENSE

    #Punis les connexions d'un neuron
    def punisConnection(self, neuron):
        if self.connections[neuron] > RECOMPENSE + BASE_WEIGHT:
            self.connections[neuron] -= RECOMPENSE
        else:
            self.connections[neuron] = BASE_WEIGHT

    #Modifié de sa version original pour un résultat plus condensé
    def printConnections(self):
        print("Connections of", self.asString() + ":")
        for neuron in self.connections:
            if self.connections[neuron] != BASE_WEIGHT:
                sys.stdout.write("[" + neuron.asString() + " " + str(self.connections[neuron]) + "] ")
        sys.stdout.write('\n')
    def asString(self):
        return "N" + str(self.index)

    # Choisi aléatoirement un neuron parmis des connexions,
    # en favorisant la connexion la plus lourde.
    def weighted_choice(self, connections):
        # Somme total du poid des connexions
        total = sum(w for c, w in connections.items())
        r = random.uniform(0, total)
        upto = 0
        for c, w in connections.items():
            if upto + w >= r:
                return c
            upto += w

    #Agrège les connexions de deux neurones
    def agregNeuron(self, neuron2):
        for c, w in self.connections.items():
            for c2, w2 in neuron2.connections.items():
                if c.index == c2.index:
                    self.connections[c] += w2


#Surchargement de la classe NeuronNetwork opérant la réduction de poids
class PNeuronNetwork(NeuronNetwork):
    def __init__(self, maxDist, nbSticks):
        super().__init__(maxDist, nbSticks)

    def punisConnections(self):
        for neuron1,neuron2 in self.path.items():
            neuron1.punisConnection(neuron2)
        self.initPath()
