class puzzleteil:

    def puzzleteil(self,links:int,mitte:int,rechts:int):
        self.links =links
        self.mitte = mitte
        self.rechts = rechts
        self.gesamtesTeil = [links, mitte, rechts]

    def drehen(self, richtung = "links"):
        if richtung =="links":
            temp = self.links
            self.links = self.rechts
            self.rechts = self.mitte
            self.mitte = temp
            self.gesamtesTeil = [self.links, self.mitte, self.rechts]
        else:
            temp = self.links
            self.links = self.mitte
            self.mitte = self.rechts
            self.rechts = temp
            self.gesamtesTeil = [self.links, self.mitte, self.rechts]


