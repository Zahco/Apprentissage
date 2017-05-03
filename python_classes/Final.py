from Game import *

#Script final permettant le lancement du jeu.
#Le Joueur joue contre le niveau de CPU qu'il souhaite.
#S'il joue contre un hard, un réseau de neurone est chargé (nous pouvons changer le réseau de neurone
#dans l'appelle du script de lancement)
#Le Joueur peut choisir s'il commence à jouer en premier ou non.
def final(sticks, network):
    print("Welcome to Nim's game!")
    print("Please input your name:")
    name = input("Name? : ")
    print("Please input which mode you'd like to play:")
    print(" easy, medium, hard")
    mode = input("Mode? : ")
    while mode not in ['easy', 'medium', 'hard']:
        print("Invalid mode, please choose a correct mode from the following: ")
        print(" easy, medium, hard")
        mode = input("Mode?:")
    p = HumanPlayer(name)
    p1 = CPUPlayer("Nim", mode, sticks)
    if p1.mode == 'hard':
        p1.netw = pickle.load(open(network, "rb"))
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


final(15, "best.nnw")
