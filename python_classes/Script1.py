from Game import *

#Le Joueur joue une partie contre un CPU easy.
#Le Joueur commence.
# sticks : nombre de bâtons
def script1(sticks):
    p = HumanPlayer("human")
    p1 = CPUPlayer("CPU", "easy", sticks)
    Game(sticks).start(p, p1, True)

script1(15)
