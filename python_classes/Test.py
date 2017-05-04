from Game import *

def test(sticks, learningRange, firstMode, secondMode):
    first = CPUPlayer("CPU", firstMode, sticks)
    second = CPUPlayer("CPU", secondMode, sticks)
    for i in range(0, learningRange):
        Game(sticks).start(first, second, False)
    if (firstMode == "hard"):
        first.netw.printAllConnections()
    print("")
    if (secondMode == "hard"):
        second.netw.printAllConnections()

#test(15, 10000, "hard", "medium")
#test(15, 50000, "easy", "hard")


def test2(sticks, learningRange, firstMode, secondMode):
    first = CPUPlayer("CPU", firstMode, sticks)
    second = HumanPlayer("human")
    for i in range(0, learningRange):
        Game(sticks).start(first, second, False)
    if (firstMode == "hard"):
        first.netw.printAllConnections()
    print("")
    if (secondMode == "hard"):
        second.netw.printAllConnections()

#test2(15, 10000, "hard", "medium")
while 1:
    test2(15, 1, "hard", "e")
