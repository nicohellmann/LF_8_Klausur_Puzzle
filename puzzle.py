from puzzleteil import puzzleteil
class puzzle:
    
    def puzzle(self,*,puzzleteile:list):
        try:
            self.teile = [puzzleteile]
        except:
            self.teile = []

    