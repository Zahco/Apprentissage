from Game import *

# Méthode permettant de faire les graphiques que nous utilisons dans notre rapport
# Nous faisons une moyenne sur 50 pour éliminer au maximum le facteur aléatoire
# ! Attention ! : Ces tests prennent longtemps (5-10 min) (surtout pour les 3 dernières phases)
def chartMaker(sticks):
    sum = 0
    for i in range(0, 50):
        sum += learningPhase(100, sticks)
    print(sum / 50)
    sum = 0
    for i in range(0, 50):
        sum += learningPhase(500, sticks)
    print(sum / 50)
    sum = 0
    for i in range(0, 50):
        sum += learningPhase(1000, sticks)
    print(sum / 50)
    sum = 0
    for i in range(0, 50):
        sum += learningPhase(5000, sticks)
    print(sum / 50)
    sum = 0
    for i in range(0, 50):
        sum += learningPhase(10000, sticks)
    print(sum / 50)
    sum = 0
    for i in range(0, 50):
        sum += learningPhase(50000, sticks)
    print(sum / 50)
    sum = 0
    for i in range(0, 50):
        sum += learningPhase(100000, sticks)
    print(sum / 50)
    sum = 0


# Méthode lancant effectivement les tests de ChartMaker
def learningPhase(LearningSet, sticks):
    p = HumanPlayer("human")
    p1 = CPUPlayer("CPU", "hard", sticks)
    p2 = CPUPlayer("CPU", "medium", sticks)
    for i in range(0, LearningSet):
        Game(sticks).start(p1, p2, False)
    return ((p1.getNbWin() / (LearningSet)) * 100)

chartMaker(15)
