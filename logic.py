# Import necessary modules
import random

class Data():
    def __init__(self) -> None:
        self.holes = {
        'hole7': [(0, 7.5, 1), (0, 9.5, 1)],
        'hole8' : [(0, 4.5, 1), (0, 6, 1)],
        'hole9' : [(0, 1, 1), (0, 3, 1)],
        'hole10' : [(0, -2, 1), (0, 0, 1)],
        'hole11' : [(0, -5-5, 1), (0, -3, 1)],
        'hole12' : [(0, -8.5, 1), (0, -6.5, 1)],
        'bank1' : [(0, 12.5, 1), (2.5, 11.5, 1)],
        'bank2' : [(0, -10.5, 1), (3, -11.5, 1)],
        "hole1":[(3, 7.5, 1), (3, 9.5, 1)], 
        "hole2":[(3, 4, 1), (3, 6, 1)], 
        "hole3":[(3, 1, 1), (3, 3, 1)], 
        "hole4":[(3, -2, 1), (3, 0, 1)], 
        "hole5":[(3, -5.3, 1), (3, -3.3, 1)], 
        "hole6":[(3, -8.3, 1), (3, -6.5, 1)]
        }
        self.beads = {}
        self.beadsList = ['b' + str(i+1) for i in range(48)]

    def initBeads(self, seedNum = 4):
        """A function to initialize the beads."""
        self.positionList = []
        for name, pos in list(self.holes.items())[:12]:
            xmin, ymin, zmin = pos[0]
            xmax, ymax, zmax = pos[1]
            xpos = [xmin + ((xmax - xmin) / (seedNum - 1)) * (i -1) for i in range(1, seedNum + 1)]
            ypos = [ymin + ((ymax - ymin) / (seedNum - 1)) * (i -1) for i in range(1, seedNum + 1)]
            zpos = [zmin + ((zmax - zmin) / (seedNum - 1)) * (i -1) for i in range(1, seedNum + 1)]

            for i in range(seedNum):
                self.positionList.append((xpos[i], ypos[i], zpos[i]))

        self.beads = dict(zip(self.beadsList, self.positionList))
        return self.beads

class Player():
    def __init__(self, side) -> None:
        self.playerNames = ['Darlene', 'Eliot', 'Alderson', 'Whiterose', 'Tyrell', 'Shayla', 'Mr. Robot', 'Angela']
        self.side = side
        self.player1, self.player2 = tuple(random.choices(self.playerNames))
        self.bank1 = 0
        self.bank2 = 0
        self.currentPlayer = random.choice(self.player1, self.player2)
    
    def addBank1(self, value):
        self.bank1 += value

    def addBank2(self, value):
        self.bank2 += value
    
    def giveTurn(self, status):
        self.isPlaying = status

class Game():
    def __init__(self) -> None:
        self.board = [4 for _ in range(12)]
        self.upsideIdx = [idx for idx in range(6)]
        self.downsideIdx = [idx for idx in range(6, 12)]
        self.changedIdx = []
        p = Player()

    def displayGame(self):
        print(self.board[0:6], self.board[6:12], sep = "\n")

    def endGame(self):
        pass

    def getBoard(self):
        return self.board

    def startGame(self):
        self.displayGame()

        move = int(input("Choose a pit from 1 to 12: "))
        
        if move in self.upsideIdx:
            self.player1 = Player(self.upsideIdx)
        elif move in self.downsideIdx:
            self.player2 = Player(self.downsideIdx)
        
        while True:
            pass

if __name__ == "__main__":
    d = Data()
    d.initBoard()
