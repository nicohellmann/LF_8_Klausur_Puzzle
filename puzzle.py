from puzzleteil import Puzzleteil
class puzzle:
    
    def puzzle(self,*,Puzzleteile:list):
        try:
            self.teile = [Puzzleteile]
        except:
            self.teile = []
        
        self.lösung = []
        
        self.lösung.append([None]*1)
        self.lösung.append([None]*3)
        self.lösung.append([None]*5)

    def teilPasst(self,teil:Puzzleteil,zeile:int,position:int):
        stimmt = True
        if(self.lösung[zeile][position].spitzeUnten == True):
            try:
                if(self.lösung[zeile][position].mitte != self.lösung[zeile-1][position-1].mitte *-1  ):
                    stimmt = False
            except:
                pass
            try:
                if(self.lösung[zeile][position].links != self.lösung[zeile][position-1].rechts *-1 ):
                    stimmt = False
            except:
                pass
            try:
                if(self.lösung[zeile][position].rechts != self.lösung[zeile][position+1].links *-1 ):
                    stimmt = False
            except:
                pass
        else:
            try:
                if(self.lösung[zeile][position].mitte != self.lösung[zeile+1][position+1].mitte *-1  and self.lösung[zeile][position].links != self.lösung[zeile][position-1].rechts *-1  and self.lösung[zeile][position].rechts != self.lösung[zeile][position+1].links *-1 ):
                    stimmt = False
            except:
                pass
            try:
                if(self.lösung[zeile][position].links != self.lösung[zeile][position-1].rechts *-1 ):
                    stimmt = False
            except:
                pass
            try:
                if(self.lösung[zeile][position].rechts != self.lösung[zeile][position+1].links *-1 ):
                    stimmt = False
            except:
                pass

        return stimmt



    def lösungKontrollieren(self):
        stimmt = True
        for i in range(0,len(self.lösung)):
            for k in range(0,len(self.lösung[i])):
                pass

    


    def lösungerstellen(self,zeile):
        if self.lösungKontrollieren == True:
            return True
        for k in range(0,len(self.teile)):
            for i in range(0,len(self.lösung[zeile])):

                if i%2==0:
                    self.teile[k].spitzeRunterDrehen()
                if(self.teilPasst(self.teile[k],zeile,i)):
                    self.lösung[zeile][i] = self.teile.pop(k)

                    if (self.lösungerstellen( zeile + 1) == True):
                        return True
                    
                    self.lösung[zeile][i] = None
                    
        return False
                    
        
            