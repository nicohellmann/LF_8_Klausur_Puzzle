from puzzle import puzzle
from puzzleteil import Puzzleteil

piece1 =Puzzleteil(1,2,3)
piece2 = Puzzleteil(1,2,3,spitzeUnten=True)
piece3=Puzzleteil(4,5,6)
piece4=Puzzleteil(-6,-2,3,spitzeUnten=True)

datei = "puzzle"+str(0)+".txt"


puzzle1 = puzzle(datei)




print(puzzle1.lösungerstellen(0))
print(puzzle1.getLösung())


    


        






