# Inutile de modifier cette classe normalement
from Player import *

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
    def run(self):
        p = HumanPlayer("human")
        p1 = CPUPlayer("CPU", "medium", self.nbSticks)
        p2 = CPUPlayer("CPU", "hard", self.nbSticks)
        print("Connections: ")
        p2.netw.printAllConnections()
        print("Scores: ")
        p2.netw.printScores()
        self.LearningPhase(100)
        self.LearningPhase(500)
        self.LearningPhase(1000)
        self.LearningPhase(5000)
        self.LearningPhase(10000)
        self.LearningPhase(50000)
        self.LearningPhase(100000)
        #self.start(p2,p, True)
        #self.start(p,p2,True)
    def LearningPhase(self, LearningSet, p1, p2):
        for i in range(0,LearningSet):
            self.start(p2, p1, False)
        for i in range (0,LearningSet):
            self.start(p1,p2,False)
        print("Taux de réussite pour ",LearningSet," essais : ", (p2.getNbWin() / (LearningSet * 2)) * 100, "%")
    def LearningPhase(self, LearningSet):
        p = HumanPlayer("human")
        p1 = CPUPlayer("CPU", "medium", self.nbSticks)
        p2 = CPUPlayer("CPU", "hard", self.nbSticks)
        for i in range(0,LearningSet):
            self.start(p2, p1, False)
        for i in range (0,LearningSet):
            self.start(p1,p2,False)
        print("Taux de réussite pour ",LearningSet * 2," essais : ", (p2.getNbWin() / (LearningSet * 2)) * 100, "%")
        #print("Connections: ")
        #p2.netw.printAllConnections()
        #print("Scores: ")
        #p2.netw.printScores()
        #self.start(p2,p,True)
Game(15).run()
