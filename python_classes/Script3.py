from Game import *

#Nous observons des parties successives de toute les combinaisons entre les easy, medium et hard -
# (easy vs easy, easy vs medium...)
#Nous évaluons ensuite leur performance.
# sticks : nombre de bâtons
def script3(sticks):
    list = ['easy', 'medium', 'hard']
    for i in range(len(list)):
        for j in range(len(list)):
            p = CPUPlayer("CPU", list[i], sticks)
            p1 = CPUPlayer("CPU", list[j], sticks)
            print(list[i], " vs ", list[j])
            for v in range(0, 2000):
                Game(sticks).start(p, p1, False)
            print(list[i],"'s score :")
            print(p.getNbWin(), " / 2000")
            print(list[j],"'s score :")
            print(p1.getNbWin(), " / 2000")
            print("")
        print("---------------")

script3(15)
