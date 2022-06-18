import random

class Player():
    def __init__(self, side) -> None:
        self.playerNames = ['Darlene', 'Eliot', 'Alderson', 'Whiterose']
        self.side = side
        self.playerName = self.playerNames[random.randint(0, len(self.playerNames) - 1)]
        self.bank = 0
        self.isPlaying = False
    
    def setBank(self, value):
        self.bank += value
    
    def giveTurn(self, status):
        self.isPlaying = status
    
    def getTurn(self):
        return self.isPlaying

class Game():
    def __init__(self) -> None:
        self.board = [4 for _ in range(12)]
        self.upsideIdx = [idx for idx in range(6)]
        self.downsideIdx = [idx for idx in range(6, 12)]
        self.changedIdx = []
        self.player1 = None

    def displayGame(self):
        print(self.board[0:6], self.board[6:12], sep = "\n")

    def endGame(self):
        pass

    def getBoard(self):
        return self.board

    def startGame(self):
        self.displayGame()

        inp = int(input("Choose a pit from 1 to 12: "))
        
        if inp in self.upsideIdx:
            self.player1 = Player(self.upsideIdx)
        elif inp in self.downsideIdx:
            self.player2 = Player(self.downsideIdx)
        
        while True:
            pass

if __name__ == "__main__":
    game = Game()
    game.startGame()
    game.displayGame()
