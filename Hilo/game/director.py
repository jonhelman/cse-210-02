from game.hilo import Deck


class Director:

    def __init__(self):
  
        self.playingCard = []
        self.isPlaying = True
        self.gameScore = 300
        self.totalScore = 0

        for i in range(1):
            hiloDeck = Deck()
            self.playingCard.append(hiloDeck)

    def StartGame(self):
 
        while self.isPlaying:
            self.GetInputs()
            self.DoUpdates()
            self.DoOutputs()

    def GetInputs(self):
 
        firstCard = ""
        for i in range(len(self.playingCard)):
            hiloDeck = self.playingCard[i]
            firstCard += f"{hiloDeck.cardOne} "
        print()
        print(f"The card is {firstCard}")
        
       
    def DoUpdates(self):

        if not self.isPlaying:
            return 

        for i in range(len(self.playingCard)):
            hiloDeck = self.playingCard[i]
            hiloDeck.Draw()
            self.gameScore += hiloDeck.playerPoints 
        self.totalScore += self.gameScore

    def DoOutputs(self):
 
        if not self.isPlaying:
            return
        
        secondCard = ""
        for i in range(len(self.playingCard)):
            hiloDeck = self.playingCard[i]
            secondCard += f"{hiloDeck.cardTwo} "

        print(f"Next card was: {secondCard}")
        print(f"Your score is: {self.totalScore}")

        drawCard = input("Play Again? [y/n] ")


        self.gameScore = 0
        self.isPlaying = self.gameScore > -1

        self.isPlaying = (drawCard == "y")
