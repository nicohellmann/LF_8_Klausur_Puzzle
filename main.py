from puzzle import puzzle
from puzzleteil import Puzzleteil

piece1 =Puzzleteil(1,2,3)
piece2 = Puzzleteil(1,2,3,spitzeUnten=True)
print(piece1)


piece1.spitzeRunterDrehen()
print(piece1)
piece1.drehen(richtung="rechts")
print()
print(piece1)


