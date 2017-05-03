from Game import *
from Player import *

# Méthode permettant de faire les graphiques que nous utilisons dans notre rapport
# Nous faisons une moyenne sur 50 pour éliminer au maximum le facteur aléatoire
# ! Attention ! : Ces tests prennent longtemps (5-10 min) (surtout pour les 3 dernières phases)
def chartMaker(sticks):
    sum = 0
    list = [100,500,1000,5000,10000,50000,100000]
    for j in range(len(list)):
        sum = 0
        for i in range(0, 50):
            sum += learningPhase(list[j], sticks)
            #sum += learningPhasePunish(list[j], sticks)
        print(sum / 50)


# Méthode lancant effectivement les tests de ChartMaker
def learningPhase(LearningSet, sticks):
    p = HumanPlayer("human")
    p1 = CPUPlayer("CPU", "hard", sticks)
    p2 = CPUPlayer("CPU", "easy", sticks)
    for i in range(0, LearningSet):
        Game(sticks).start(p1, p2, False)
    return ((p1.getNbWin() / (LearningSet)) * 100)

# Méthode lancant effectivement les tests de ChartMaker
# Avec punition
def learningPhasePunish(LearningSet, sticks):
    p = HumanPlayer("human")
    p1 = CPUPlayer("CPU", "hard", sticks)
    p2 = CPUPlayer("CPU", "easy", sticks)
    p1.netw = PNeuronNetwork(MAX_DIST, sticks)
    p2.netw = PNeuronNetwork(MAX_DIST, sticks)
    for i in range(0, LearningSet):
        Game(sticks).start(p1, p2, False)
    return ((p1.getNbWin() / (LearningSet)) * 100)

chartMaker(15)
