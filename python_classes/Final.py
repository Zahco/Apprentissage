from Game import *

def Final(sticks):
    print("Welcome to Nim's game!")
    print("Please input your name:")
    name = input("Name? : ")
    print("Please input which mode you'd like to play:")
    print("1 -> easy, 2 -> medium, 3 -> hard")
    mode = input("Mode? : ")
    while mode not in ['1', '2', '3', 'easy', 'medium', 'hard']:
        print("Invalid mode, please choose a correct mode from the following: ")
        print("1 -> easy, 2 -> medium, 3 -> hard")
        mode = input("Mode?:")
    mode =switch(mode)
    p = HumanPlayer(name)
    p1 = CPUPlayer("Nim", mode, sticks)
    if hasattr(p1, 'netw'):
        p1.netw = pickle.load(open("network.nnw", "rb"))
    print("Do you wish to be first to play?")
    turn = input("1 -> yes, 2 -> no : ")
    while turn not in ['1', 'yes', '2', 'no']:
        print("Invalid option, please choose a correct turn from the follwing:")
        turn = input("1 -> yes, 2 -> no : ")
    print("Let the Game Begin!")
    if (turn in ['1', 'yes']):
        print(name, " vs Nim!")
        print(name, " starts!")
        Game(sticks).start(p, p1, True)
    else:
        print("Nim vs ", name)
        print("Nim starts!")
        Game(sticks).start(p1, p, True)


def switch(x):
    return {
        1: 'easy',
        2: 'medium',
        3: 'hard',
    }.get(x, x)

Final(15)