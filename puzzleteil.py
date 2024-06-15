class Puzzleteil:

    def __init__(self,links:int,mitte:int,rechts:int,spitzeUnten=False):
        self.links =links
        self.mitte = mitte
        self.rechts = rechts
        self.gesamtesTeil = [links, mitte, rechts]
        self.spitzeUnten = spitzeUnten

            

    def drehen(self, richtung = "links"):
        if richtung =="links":
            if (self.spitzeUnten == False):
                temp = self.links
                self.links = self.rechts
                self.rechts = self.mitte
                self.mitte = temp
                
            else:
                temp = self.links
                self.links = self.mitte
                self.mitte = self.rechts
                self.rechts = temp
                

        else:
            if (self.spitzeUnten == False):
                temp = self.links
                self.links = self.mitte
                self.mitte = self.rechts
                self.rechts = temp
                
            else:
                temp = self.links
                self.links = self.rechts
                self.rechts = self.mitte
                self.mitte = temp
        self.gesamtesTeil = [self.links, self.mitte, self.rechts]


    def spitzeRunterDrehen(self):

        # die Ecke unten rechts wird die nach unten zeigende "Spitze" -> die linke kante wird zur mittleren
        temp = self.rechts
        self.rechts = self.links
        self.links = temp
        self.spitzeUnten = True
        self.gesamtesTeil = [self.links, self.mitte, self.rechts]

    def __str__(self) -> str:
        re=""
        if self.spitzeUnten==True:
            re = str(self.links) +" "+ str(self.rechts) +"\n"+" "+ str(self.mitte)
        else:
            re = " "+ str(self.mitte) +"\n"+str(self.links) +" "+ str(self.rechts)

        return re

    


