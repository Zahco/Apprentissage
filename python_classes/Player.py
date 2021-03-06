import random
from Neuron import *

class Player:
    def __init__(self, name):
        self.name = name
        self.nbWin = 0
    def getName(self):
        return self.name
    def getNbWin(self):
        return self.nbWin
    def addWin(self):
        self.nbWin += 1
    def addLoss(self):
        pass

class HumanPlayer(Player):
    def play(self, sticks):
        if sticks == 1:
            return 1
        else:
            correct = False
            while not correct:
                nb = input('Sticks?\n')
                try:
                    nb = int(nb)
                    if nb >= 1 and nb <= MAX_DIST and sticks - nb >= 0:
                        correct=True
                except: pass
            return nb

class CPUPlayer(Player):
    def __init__(self, name, mode, nbSticks):
        super().__init__(name)
        self.mode = mode
        self.netw = NeuronNetwork(MAX_DIST, nbSticks)
        self.previousNeuron = None
    def play(self, sticks):
        if self.mode == 'easy':
            return self.playEasy(sticks)
        elif self.mode == 'hard':
            return self.playHard(sticks)
        else:
            return self.playMedium(sticks)

    def playMedium(self, sticks):
        if sticks <= MAX_DIST + 1 and sticks >= 2:
            return sticks - 1
        else:
            return self.playRandom(sticks)

    def playEasy(self, sticks):
        return self.playRandom(sticks)

    #Joue alétoirement entre 1 et MAX_DIST bâtons
    #Cette fonction a été modifié de sa version originale (cf. rapport)
    def playRandom(self, sticks):
        if sticks >= 3:
            return random.randint(1, MAX_DIST)
        else:
            return random.randint(1, (sticks % MAX_DIST))

    def playHard(self, sticks):
        if sticks == 1:
            return 1
        if (self.previousNeuron is None):
            self.previousNeuron = self.netw.getNeuron(sticks)
        # Calcul du shift (coup joué par l'utilisateur)
        shift = self.previousNeuron.index - sticks
        # Choix du neuron
        neuron = self.previousNeuron.chooseConnectedNeuron(shift)
        # Enregistrement de la connexion au neuron (pour les futures récompenses)
        self.getNeuronNetwork().activateNeuronPath(self.previousNeuron, neuron)
        # Enregistrement du previous neuron
        self.previousNeuron = neuron
        return sticks - neuron.index



    def getNeuronNetwork(self):
        return self.netw
    # Réinitialise le joueur et récompense le réseau de neuron
    def addWin(self):
        super().addWin()
        self.netw.recompenseConnections()
        self.previousNeuron = None
        self.netw.initPath()

    # Réinitialise le joueur
    def addLoss(self):
        super().addLoss()
        self.netw.punisConnections()
        self.previousNeuron = None
        self.netw.initPath()
