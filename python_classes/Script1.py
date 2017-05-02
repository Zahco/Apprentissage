from Game import *



def Script1(sticks):
    p = HumanPlayer("human")
    p1 = CPUPlayer("CPU", "easy", sticks)
    Game(sticks).start(p, p1, True)

Script1(15)