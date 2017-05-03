from Game import *


# Exemple d'importation d'un réseau neuronal sur un joueur 'hard' et lancement de la partie
def importAndPlay(netw, sticks):
    p = HumanPlayer("human")
    p1 = CPUPlayer("CPU", "hard", sticks)
    p1.netw = pickle.load(open(netw, "rb"))
    Game(sticks).start(p, p1, True)

importAndPlay("network.nnw", 15)