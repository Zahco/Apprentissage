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
    def run(self):
        p = HumanPlayer("human")
        p1 = CPUPlayer("CPU", "medium", self.nbSticks)
        p2 = CPUPlayer("CPU", "hard", self.nbSticks)
        #print("Connections: ")
        #p2.netw.printAllConnections()
        #print("Scores: ")
        #p2.netw.printScores()
        #self.start(p2,p, True)
        #self.start(p,p2,True)
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
        p1 = CPUPlayer("CPU", "medium", self.nbSticks)
        p2 = CPUPlayer("CPU", "hard", self.nbSticks)
        for i in range(0,LearningSet):
            self.start(p1, p2, False)
       # pickle.dump(p2.netw, open("network.nnw", "wb"))
       # print("Taux de réussite pour ",LearningSet," essais : ", (p2.getNbWin() / (LearningSet)) * 100, "%")
        return ((p1.getNbWin() / (LearningSet)) * 100)

        #print("Connections: ")
        #p2.netw.printAllConnections()
        #print("Scores: ")
        #p2.netw.printScores()
        #self.start(p2,p,True)
    def Script1(self, sticks):
        p = HumanPlayer("human")
        p1 = CPUPlayer("CPU", "easy", self.nbSticks)
        self.start(p, p1, True)
    def Script2(self, sticks):
        p = CPUPlayer("CPU", "hard", self.nbSticks)
        p1 = CPUPlayer("CPU", "hard", self.nbSticks)
        for i in range(0, 800):
            self.start(p, p1, False)
        print("Connections de p: ")
        p.netw.printAllConnections()
        print("Scores de p: ")
        p.netw.printScores()
        print("Connections de p1: ")
        p.netw.printAllConnections()
        print("Scores de p1: ")
        p.netw.printScores()
    def Script3(self, sticks):
        p = CPUPlayer("CPU", "easy", self.nbSticks)
        p1 = CPUPlayer("CPU", "easy", self.nbSticks)
        self.Scriptfor3(sticks, p,p1)
        p = CPUPlayer("CPU", "easy", self.nbSticks)
        p1 = CPUPlayer("CPU", "medium", self.nbSticks)
        self.Scriptfor3(sticks, p, p1)
        p = CPUPlayer("CPU", "easy", self.nbSticks)
        p1 = CPUPlayer("CPU", "hard", self.nbSticks)
        self.Scriptfor3(sticks, p, p1)
        p = CPUPlayer("CPU", "medium", self.nbSticks)
        p1 = CPUPlayer("CPU", "easy", self.nbSticks)
        self.Scriptfor3(sticks, p, p1)
        p = CPUPlayer("CPU", "medium", self.nbSticks)
        p1 = CPUPlayer("CPU", "medium", self.nbSticks)
        self.Scriptfor3(sticks, p, p1)
        p = CPUPlayer("CPU", "medium", self.nbSticks)
        p1 = CPUPlayer("CPU", "hard", self.nbSticks)
        self.Scriptfor3(sticks, p, p1)
        p = CPUPlayer("CPU", "hard", self.nbSticks)
        p1 = CPUPlayer("CPU", "easy", self.nbSticks)
        self.Scriptfor3(sticks, p, p1)
        p = CPUPlayer("CPU", "hard", self.nbSticks)
        p1 = CPUPlayer("CPU", "medium", self.nbSticks)
        self.Scriptfor3(sticks, p, p1)
    def Scriptfor3(self, sticks, p, p1):
        for i in range(0, 2000):
            self.start(p, p1, False)
        print("Connections de p: ")
        p.netw.printAllConnections()
        print("Scores de p: ")
        p.netw.printScores()
        print("Connections de p1: ")
        p.netw.printAllConnections()
        print("Scores de p1: ")
    def Final(self):
        print("Welcome to Nim's game!")
        print("Please input your name:")
        name = input("Name? : ")
        print("Please input which mode you'd like to play:")
        print("1 -> easy, 2 -> medium, 3 -> hard")
        mode = input("Mode? : ")
        while mode not in ['1','2','3','easy', 'medium','hard']:
            print("Invalid mode, please choose a correct mode from the following: ")
            print("1 -> easy, 2 -> medium, 3 -> hard")
            mode = input("Mode?:")
        mode = self.switch(mode)
        p = HumanPlayer(name)
        p1 = CPUPlayer("Nim", mode, self.nbSticks)
        if hasattr(p1, 'netw'):
            p1.netw = pickle.load(open("network.nnw", "rb"))
        print("Do you wish to be first to play?")
        turn = input("1 -> yes, 2 -> no : ")
        while turn not in ['1', 'yes', '2', 'no']:
            print("Invalid option, please choose a correct turn from the follwing:")
            turn = input("1 -> yes, 2 -> no : ")
        print("Let the Game Begin!")
        if (turn in ['1', 'yes']):
            self.start(p, p1, True)
        else :
            self.start(p1, p, True)


    def switch(self,x):
        return {
            1: 'easy',
            2: 'medium',
            3: 'hard',
        }.get(x,x)
Game(15).run()
#Game(15).ImportAndPlay()
#Game(15).Final()
