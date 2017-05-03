from Game import *

def printFromFile(sticks, network):
    p1 = CPUPlayer("Nim", 'hard', sticks)
    p1.netw = pickle.load(open(network, "rb"))
    p1.netw.printAllConnections()

printFromFile(15, 'punishedNetwork.nnw')
