class puzzleteil:

    def puzzleteil(self,links:int,unten:int,rechts:int):
        self.links =links
        self.unten = unten
        self.rechts = rechts
        self.gesamtesTeil = [links, unten, rechts]

    def drehen(self, richtung = "links"):
        if richtung =="links":
            temp = self.links
            self.links = self.rechts
            self.rechts = self.unten
            self.unten = temp
            self.gesamtesTeil = [self.links, self.unten, self.rechts]
        else:
            temp = self.links
            self.links = self.unten
            self.unten = self.rechts
            self.rechts = temp


