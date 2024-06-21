from puzzleteil import Puzzleteil
class puzzle:
    
    def __init__(self,datei:str):
        file = open(datei,'r')
        self.teile= []
        for zeile in file:    
            temp = zeile.split(" ")
            temp2= []
            for i in range(0,3):
                temp2.append(int(temp[i]))
        
            self.teile.append(Puzzleteil(1,1,1,list=temp2))
        self.lösung = []
        
        self.lösung.append([None]*1)
        self.lösung.append([None]*3)
        self.lösung.append([None]*5)

    def teilPasst(self,teil:Puzzleteil,zeile:int,position:int):
        stimmt = True
        if self.lösung[zeile][position]!=None:
            return False
        if(position%2==0):
                teil.spitzeHochDrehen()
        if(position%2==1):
                teil.spitzeRunterDrehen()
        for j in range(3):
            stimmt = True
            if(teil.spitzeUnten == True):
                
                
                if(teil.mitte != self.lösung[zeile-1][position-1].mitte *(-1)  ):
                    
                    stimmt = False
                
                
                
                if(teil.links != self.lösung[zeile][position-1].rechts *(-1) ):
                        
                        stimmt = False
                
                try:
                    if(teil.rechts != self.lösung[zeile][position+1].links *(-1) ):
                       
                        stimmt = False
                except:
                    pass
            else:
                
                
                try:
                    if(teil.mitte != self.lösung[zeile+1][position+1].mitte *(-1)):  
                        
                        stimmt = False
                except:
                    pass
                if position==0:
                    pass
                else:
                    if(teil.links != self.lösung[zeile][position-1].rechts *(-1) ):
                            
                        stimmt = False
                
                try:
                    if(teil.rechts != self.lösung[zeile][position+1].links *(-1) ):
                        
                        stimmt = False
                except:
                    pass

            if stimmt:
                break
            else:
                teil.drehen()

        return stimmt
    
    def getPuzzleteile(self):
        temp = []
        for i in range(0,len(self.teile)):
            temp2=[]
            for k in  range(3):
                temp2.append(self.teile[i].gesamtesTeil[k])

            temp.append(temp2)

        return temp
    
    def getLösung(self):
        temp = []
        for i in range(0,len(self.lösung)):
            temp2=[]
            for k in  range(0,len(self.lösung[i])):
                if(self.lösung[i][k])==None:
                    temp2.append(None)
                else:
                    
                    temp2.append(self.lösung[i][k].gesamtesTeil)

            temp.append(temp2)

        return temp



    def lösungKontrollieren(self):
        stimmt = True
        for i in range(0,len(self.lösung)):
            for k in range(0,len(self.lösung[i])):
                if self.lösung[i][k]== None: return False
                # if self.lösung[i][k].spitzeUnten==False:
                #     try:
                #         if self.lösung[i][k].links != self.lösung[i][k-1].rechts *(-1):
                #             stimmt=False
                #     except:
                #         pass
                #     try:
                #         if self.lösung[i][k].rechts != self.lösung[i][k+1].links *(-1):
                #             stimmt=False
                #     except:
                #         pass
                #     try:
                #         if self.lösung[i][k].mitte != self.lösung[i+1][k+1].mitte *(-1):
                #             stimmt=False
                #     except:
                #         pass
                
                # if self.lösung[i][k].spitzeUnten==True:
                #     try:
                #         if self.lösung[i][k].links != self.lösung[i][k-1].rechts *(-1):
                #             stimmt=False
                #     except:
                #         pass
                #     try:
                #         if self.lösung[i][k].rechts != self.lösung[i][k+1].links *(-1):
                #             stimmt=False
                #     except:
                #         pass
                #     try:
                #         if self.lösung[i][k].mitte != self.lösung[i-1][k-1].mitte *(-1):
                #             stimmt=False
                #     except:
                #         pass
        return stimmt
    def reihePasst(self,zeile):
        counter =0
        for i in range(0,len(self.lösung[zeile])):
            if self.lösung[zeile][i]==None:
                counter +=1
        if counter ==0:
            return True
        else:
            return False

    def teillösung(self,zeile,position):
        if self.reihePasst(zeile):
            return True
        for k in range(0,len(self.teile)):
        
        
            
            if self.teilPasst(self.teile[k],zeile,position):
                
                
                
                
                self.lösung[zeile][position] = self.teile[k]
                
                if self.teillösung(zeile,position+1) ==True:
                    return True
                self.lösung[zeile][position] = None
                
            


        return False

    def lösungerstellen(self,zeile):
        
        if self.lösungKontrollieren() == True:
            return True
        
        if(self.teillösung(zeile,0)):
                        
            if (self.lösungerstellen( zeile + 1) == True) :
                return True
                        
                        
            #self.lösung[zeile][position] = None
                    
                    
        return False
                    
        
            