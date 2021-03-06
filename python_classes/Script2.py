from Game import *

#Deux CPU hards jouent l'un contre l'autre pendant 800 parties.
#Nous évaluons ensuite leurs nombres de victoire ainsi que leur réseaux de neurones
# sticks : nombre de bâtons
def script2(sticks):
    p = CPUPlayer("CPU", "hard", sticks)
    p1 = CPUPlayer("CPU", "hard", sticks)
    for i in range(0, 800):
        Game(sticks).start(p, p1, False)
    print("Nombres de victoires de p:")
    print(p.getNbWin(), " / 800")
    print("")
    print("Connections de p: ")
    p.netw.printAllConnections()
    print("")
    print("Connections neuronales pondérées de p: ")
    p.netw.printScores()
    print("")
    print("----------------------------------------")
    print("")
    print("Nombres de victoires de p1:")
    print(p1.getNbWin(), " / 800")
    print("")
    print("Connections de p1: ")
    p1.netw.printAllConnections()
    print("")
    print("Connections neuronales pondérées de p1: ")
    p1.netw.printScores()

script2(15)
