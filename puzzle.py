from puzzleteil import puzzleteil
class puzzle:
    
    def puzzle(self,*,puzzleteile:list):
        try:
            self.teile = [puzzleteile]
        except:
            self.teile = []

        self.lösung = []

    def teilPasst(self,zeile:int,position:int):
        stimmt = False
        if(self.lösung[zeile][position].spitzeUnten == True):
            if(self.lösung[zeile][position].mitte == self.lösung[zeile-1][position-1].mitte and self.lösung[zeile][position].links == self.lösung[zeile][position-1].rechts and self.lösung[zeile][position].rechts == self.lösung[zeile][position+1].links):
                stimmt = True
        else:
            if(self.lösung[zeile][position].mitte == self.lösung[zeile+1][position+1].mitte and self.lösung[zeile][position].links == self.lösung[zeile][position-1].rechts and self.lösung[zeile][position].rechts == self.lösung[zeile][position+1].links):
                stimmt = True
        return stimmt



    def lösungKontrollieren(self):
        stimmt = True
        for i in range(0,len(self.lösung)):
            for k in range(0,len(self.lösung[i])):
                pass

    


    def lösungerstellen(self):
        foundPiece = False
        temp = []
        temp.append(self.teile[0])
        self.lösung.append(temp)
        for i in range(0,len(self.teile)):
            