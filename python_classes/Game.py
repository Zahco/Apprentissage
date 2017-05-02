# Inutile de modifier cette classe normalement
from Player import *
import pickle

class Game:
    def __init__(self, nbSticks):
        self.nbSticks = nbSticks
    def start(self, player1, player2, verbose):
        if verbose:
            print("New game")
        sticks = self.nbSticks
        currp = player1
        while sticks > 0:
            if verbose:
                print("Remaining sticks:", sticks)
            n = currp.play(sticks)
            if n < 1 or n > 3:
                print("Error")
            if verbose:
                print(currp.getName(), " takes ", n)
            sticks -= n
            if currp == player1:
                currp = player2
            else:
                currp = player1

        if verbose:
            print(currp.getName(), " wins!")
        if player1 == currp:
            player1.addWin()
            player2.addLoss()
        else:
            player1.addLoss()
            player2.addWin()

    def ChartMaker(self):
        sum = 0
        for i in range(0, 50):
            sum += self.LearningPhase(100)
        print(sum / 50)
        sum = 0
        for i in range(0, 50):
            sum += self.LearningPhase(500)
        print(sum / 50)
        sum = 0
        for i in range(0, 50):
            sum += self.LearningPhase(1000)
        print(sum / 50)
        sum = 0
        for i in range(0, 50):
            sum += self.LearningPhase(5000)
        print(sum / 50)
        sum = 0
        for i in range(0, 50):
            sum += self.LearningPhase(10000)
        print(sum / 50)
        sum = 0
        for i in range(0, 50):
            sum += self.LearningPhase(50000)
        print(sum / 50)
        sum = 0
        for i in range(0, 50):
            sum += self.LearningPhase(100000)
        print(sum / 50)
        sum = 0

    def ImportAndPlay(self):
        p = HumanPlayer("human")
        p1 = CPUPlayer("CPU", "hard", self.nbSticks)
        p1.netw = pickle.load( open( "network.nnw", "rb"))
        self.start(p, p1, True)
    def LearningPhase(self, LearningSet):
        p = HumanPlayer("human")
        p1 = CPUPlayer("CPU", "hard", self.nbSticks)
        p2 = CPUPlayer("CPU", "medium", self.nbSticks)
        for i in range(0,LearningSet):
            self.start(p1, p2, False)
        return ((p1.getNbWin() / (LearningSet)) * 100)

Game(15).ChartMaker()
#Game(15).ImportAndPlay()

