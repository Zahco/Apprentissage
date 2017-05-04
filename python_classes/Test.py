from Game import *

def test(sticks, learningRange):
    hard = CPUPlayer("CPU", "hard", sticks)
    medium = CPUPlayer("CPU", "medium", sticks)
    for i in range(0, learningRange):
        Game(sticks).start(medium, hard, False)
    hard.netw.printAllConnections()

test(15, 10000)
