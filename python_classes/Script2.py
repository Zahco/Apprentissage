from Game import *

def Script2(sticks):
    p = CPUPlayer("CPU", "hard", sticks)
    p1 = CPUPlayer("CPU", "hard", sticks)
    for i in range(0, 800):
        Game(sticks).start(p, p1, False)
    print("Connections de p: ")
    p.netw.printAllConnections()
    print("Scores de p: ")
    p.netw.printScores()
    print("Connections de p1: ")
    p.netw.printAllConnections()
    print("Scores de p1: ")
    p.netw.printScores()

Script2(15)