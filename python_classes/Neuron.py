import random
from copy import copy

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

    def makeConnections(self, maxDist, nbSticks, baseWeight):
        # index != 15 , nb = 7
        if self.index != nbSticks:
            nb = maxDist * 2 + 1
        else: # pour index = 15, nb = 4
            nb = maxDist + 1
        for i in range(1, nb):
            neuron = self.network.getNeuron(self.index - i)
            # Si le neuron existe on crée une connexion
            if neuron != None:
                self.connections[neuron] = baseWeight

    # Choisi le neuron à jouer avec la méthode weighted_choice
    # Le neuron doit être atteignable (vérifié par testNeuron)
    # Condition d'arret:
    # 0 <= connectionsClone.len <= connections.len
    def chooseConnectedNeuron(self, shift):
        connectionsClone = copy(self.connections)
        neuron = self.weighted_choice(connectionsClone)
       # print("shift: ", shift, " - index: ", neuron.index)
        while (len(connectionsClone) > 0 and not neuron.testNeuron(self.index-shift)):
            connectionsClone.pop(neuron)
            neuron = self.weighted_choice(connectionsClone)
          #  print("index courrent: ", self.index," - shift: ", shift, " - index jouable ?: ", neuron.index)
        return neuron

    def testNeuron(self, inValue):
        dif = inValue - self.index
        return dif >= 1 and dif <= 3

    # Ajoute une récompense au poid de la connexion avec un neuron donné
    def recompenseConnection(self, neuron):
        self.connections[neuron] += RECOMPENSE

    def printConnections(self):
        print("Connections of", self.asString() + ":")
        for neuron in self.connections:
            print(neuron.asString(), self.connections[neuron])
    def asString(self):
        return "N" + str(self.index)

    # Choisi une aléatoirement un neuron parmis des connexions
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
