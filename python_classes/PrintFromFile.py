from Game import *

#Affiche toutes les connexions du réseau de neuron présent dans le fichier
def printFromFile(sticks, network):
    p1 = CPUPlayer("Nim", 'hard', sticks)
    p1.netw = pickle.load(open(network, "rb"))
    p1.netw.printAllConnections()

printFromFile(15, 'network.nnw')
#printFromFile(15, 'agregNetwork.nnw')
#printFromFile(15, 'punishedNetwork.nnw')
