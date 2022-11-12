import random


class Deck:

    def __init__(self):

        self.cardOne = random.randint(1, 13)
        self.cardTwo = random.randint(1, 13)
        self.playerPoints = 0
        self.hiLo = " "

    def Draw(self):

        self.cardTwo = random.randint(1, 13)

        self.hiLo = " "
        self.hiLo = input("Higher or lower? [h/l] ")

        if self.hiLo == "h" and self.cardTwo > self.cardOne:
            self.playerPoints =+ 100
        elif self.hiLo == "h" and self.cardTwo < self.cardOne:
            self.playerPoints =- 75

        elif self.hiLo == "l" and self.cardTwo < self.cardOne:
            self.playerPoints =+ 100
        elif self.hiLo == "l" and self.cardTwo > self.cardOne:
            self.playerPoints =- 75

        elif self.hiLo == "h" and self.cardTwo == self.cardOne:
            self.playerPoints =+ 0

        elif self.hiLo == "l" and self.cardTwo == self.cardOne:
            self.playerPoints =+ 0
        
        self.cardOne = self.cardTwo