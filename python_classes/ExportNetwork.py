from Game import *
#from Player import *

#Permet la création de notre réseau de neurone 'hard' le plus efficace.
#Nous créons deux réseaux de neurones:
#Le premier jouant en premier contre un hard
#Le deuxième jouant en deuxième contre un medium
#Nous agrégeons les deux en un dernier réseau de neurone capable de s'adapter aux
#différentes situations (cf. le rapport)
def exportNetwork(learningRange, sticks, network):
    answer = 'No'
    while answer not in ['1', 'yes', 'Yes', 'y', 'Y']:
        p = CPUPlayer("CPU", "hard", sticks)
        p1 = CPUPlayer("CPU", "hard", sticks)
        p2 = CPUPlayer("CPU", "hard", sticks)
        p3 = CPUPlayer("CPU", "medium", sticks)
        for i in range(0, learningRange):
            Game(sticks).start(p1, p, False)
        p1.netw.printAllConnections()
        print("")
        print("Succes rate : ", (p1.getNbWin() / (learningRange)) * 100)
        print("")
        for i in range(0, learningRange):
            Game(sticks).start(p3, p2, False)
        p2.netw.printAllConnections()
        print("")
        print("Succes rate : ", (p2.getNbWin() / (learningRange)) * 100)
        print("")
        p1.netw.agregAllNeurons(p2.netw)
        p1.netw.printAllConnections()
        print("Are you satisfied with this neuronal network?")
        print("1 -> Yes, 2 -> No : ")
        answer = input("")
    pickle.dump(p1.netw, open(network, "wb"))

def exportPunishedNetwork(learningRange, sticks, network):
    answer = 'No'
    while answer not in ['1', 'yes', 'Yes', 'y', 'Y']:
        p = CPUPlayer("CPU", "hard", sticks)
        p1 = CPUPlayer("CPU", "hard", sticks)
        p2 = CPUPlayer("CPU", "hard", sticks)
        p3 = CPUPlayer("CPU", "medium", sticks)
        p1.netw = PNeuronNetwork(MAX_DIST, sticks)
        p2.netw = PNeuronNetwork(MAX_DIST, sticks)
        p.netw = PNeuronNetwork(MAX_DIST, sticks)
        for i in range(0, learningRange):
            Game(sticks).start(p1, p, False)
        p1.netw.printAllConnections()
        print("")
        print("Succes rate : ", (p1.getNbWin() / (learningRange)) * 100)
        print("")
        for i in range(0, learningRange):
            Game(sticks).start(p3, p2, False)
        p2.netw.printAllConnections()
        print("")
        print("Succes rate : ", (p2.getNbWin() / (learningRange)) * 100)
        print("")
        p1.netw.agregAllNeurons(p2.netw)
        p1.netw.printAllConnections()
        print("Are you satisfied with this neuronal network?")
        print("1 -> Yes, 2 -> No : ")
        answer = input("")
    pickle.dump(p1.netw, open(network, "wb"))

exportNetwork(100000, 15, "network.nnw")
#exportPunishedNetwork(100000, 15, "punishedNetwork.nnw")