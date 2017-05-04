from Game import *

def test(sticks):
    while(True):
        p = CPUPlayer("CPU", "hard", sticks)
        p1 = HumanPlayer("bob")
        Game(sticks).start(p1, p, True)
        p.netw.printAllConnections()

test(15)
