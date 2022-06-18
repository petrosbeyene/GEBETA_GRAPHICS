# Import necessary modules
import random


class Data():
    def __init__(self) -> None:
        self.holes = {
            "hole1": [(2.5, 8.0, 1), (3.2, 9.0, 1)],
            "hole2": [(2.5, 4.8, 1), (3.2, 5.8, 1)],
            "hole3": [(2.5, 1.5, 1), (3.2, 2.5, 1)],
            "hole4": [(2.5, -1.8, 1), (3.2, -0.6, 1)],
            "hole5": [(2.5, -4.9, 1), (3.2, -3.8, 1)],
            "hole6": [(2.3, -8, 1), (3.2, -7.2, 1)],
            'hole7': [(-0.8, 8, 1), (0, 9, 1)],
            'hole8': [(-0.7, 4.7, 1), (0, 6, 1)],
            'hole9': [(-0.8, 1.5, 1), (0, 2.7, 1)],
            'hole10': [(-0.7, -1.7, 1), (0, -0.5, 1)],
            'hole11': [(-0.7, -4.8, 1), (0, -3.5, 1)],
            'hole12': [(-0.8, -8.2, 1), (0, -7.2, 1)],
        }
        self.banks = {
            'bank1': [(0.3, 11.5, 1), (2.2, 12.5, 1)],
            'bank2': [(0.3, -11.3, 1), (2.5, -10.5, 1.5)],
        }
        self.winHoles = {
            'hole1': [(113, 209), (165, 239)],
            'hole2': [(223, 321), (165, 239)],
            'hole3': [(333, 430), (165, 239)],
            'hole4': [(439, 538), (165, 239)],
            'hole5': [(547, 645), (165, 239)],
            'hole6': [(657, 751), (165, 239)],
            'hole7': [(111, 207), (270, 346)],
            'hole8': [(219, 316), (270, 346)],
            'hole9': [(324, 422), (270, 346)],
            'hole10': [(435, 529), (270, 346)],
            'hole11': [(538, 644), (265, 346)],
            'hole12': [(654, 753), (270, 346)]
        }
        self.beads = {}

        # initialize Beads
        self.setBeads()

    def setBeads(self, board=[4 for i in range(12)], banks = None):
        """A function to initialize the beads."""
        self.beadsList = ['b' + str(i + 1) for i in range(48)]
        self.positionList = []

        idx = 0
        for name, pos in list(self.holes.items()):
            xmin, ymin, zmin = pos[0]
            xmax, ymax, zmax = pos[1]

            if board[idx] == 1:
                xdif = 0
                ydif = 0
                zdif = 0
            else:
                xdif = (xmax - xmin) / (board[idx] - 1)
                ydif = (ymax - ymin) / (board[idx] - 1)
                zdif = (zmax - zmin) / (board[idx] - 1)

            xpos = [xmin + (xdif) * (i - 1) for i in range(1, board[idx] + 1)]
            ypos = [ymin + (ydif) * (i - 1) for i in range(1, board[idx] + 1)]
            zpos = [zmin + (zdif) * (i - 1) for i in range(1, board[idx] + 1)]

            for i in range(board[idx]):
                self.positionList.append((xpos[i], ypos[i], zpos[i]))
            idx += 1


        if banks != None:
            idx = 0
            for name, pos in list(self.banks.items()):
                xmin, ymin, zmin = pos[0]
                xmax, ymax, zmax = pos[1]

                xdif = (xmax - xmin) / (banks[idx] - 1)
                ydif = (ymax - ymin) / (banks[idx] - 1)
                zdif = (zmax - zmin) / (banks[idx] - 1)
                xpos = [xmin + (xdif) * (i - 1) for i in range(1, banks[idx] + 1)]
                ypos = [ymin + (ydif) * (i - 1) for i in range(1, banks[idx] + 1)]
                zpos = [zmin + (zdif) * (i - 1) for i in range(1, banks[idx] + 1)]

                for i in range(banks[idx]):
                    self.positionList.append((xpos[i], ypos[i], zpos[i]))
                idx += 1

        self.beads = dict(zip(self.beadsList, self.positionList))

    def getBeads(self):
        return self.beads

    def getHoles(self):
        return self.holes

    def getWinHoles(self):
        return self.winHoles

class Player():
    def __init__(self, name, side) -> None:
        self.name = name
        self.side = side
        self.bank = 0

    def addBank(self, value):
        self.bank += value

    def getSide(self):
        return self.side

    def getBank(self):
        return self.bank


class Game():
    def __init__(self) -> None:
        # Game datas
        self.dataObj = Data()
        self.beads = self.dataObj.getBeads()
        self.holes = self.dataObj.getHoles()
        self.winHoles = self.dataObj.getWinHoles()

        # Game materials
        self.board = [4 for _ in range(12)]
        self.upsideIdx = [idx for idx in range(6)]
        self.downsideIdx = [idx for idx in range(6, 12)]
        self.changedIdx = []
        self.holeNum = None
        self.isEndGame = False

        # 2 PLayers
        playerNames = ['Darlene', 'Eliot', 'Alderson', 'Whiterose', 'Tyrell', 'Shayla', 'Mr. Robot', 'Angela']
        names = random.choices(playerNames, k=2)

        self.player1 = Player(names[0], self.upsideIdx)
        self.player2 = Player(names[1], self.downsideIdx)

        self.currentPlayer = self.player1
        self.otherPlayer = self.player2

        self.players = [self.currentPlayer, self.otherPlayer]

    def changePlayer(self):
        self.currentPlayer, self.otherPlayer = self.otherPlayer, self.currentPlayer

    def getCurrentPlayer(self):
        return self.currentPlayer.name

    def isValidMove(self, clickPos):
        # side check
        idx = 0
        x, y = clickPos
        for name, pos in list(self.winHoles.items()):
            xmin, xmax = pos[0]
            ymin, ymax = pos[1]
            if xmin <= x <= xmax:
                if ymin <= y <= ymax:
                    self.holeNum = idx
                    self.startGame()
            idx += 1
        return False

    def displayGame(self):
        print(self.board[0:6], self.board[6:12], sep="\n")
        print(self.currentPlayer.name, self.currentPlayer.bank)
        print(self.otherPlayer.name, self.otherPlayer.bank)
        print("Playing: {}".format(self.currentPlayer.name))

    def endGame(self):
        self.isEndGame = True

    def startGame(self):
        # Game loop
        while self.board[self.holeNum] != 0 and self.holeNum in self.currentPlayer.side and self.isEndGame != True:
            start_seed = self.holeNum

            # Seeding loop
            while True:
                end_seed = start_seed + self.board[start_seed]
                self.board[start_seed] = 0
                self.changedIdx.append(start_seed)

                for seed_idx in range(start_seed + 1, end_seed + 1):
                    if seed_idx > 11:
                        seed_idx = seed_idx % 12
                    self.changedIdx.append(seed_idx)
                    self.board[seed_idx] = self.board[seed_idx] + 1

                # Debugger lines - to see each step
                # print(self.board[0:6])
                # print(self.board[6:12])
                # print()

                if self.board[seed_idx] == 1:
                    self.changePlayer()
                    break
                elif self.board[seed_idx] == 4:
                    if seed_idx in self.currentPlayer.getSide():
                        self.currentPlayer.addBank(4)
                        self.changePlayer()
                    elif seed_idx in self.otherPlayer.getSide():
                        self.otherPlayer.addBank(4)
                        self.changePlayer()
                    break
                elif self.board[seed_idx] != 4 and self.board[start_seed] != 1:
                    start_seed = seed_idx
                    continue

            # calculate the sum of beads in the sides of the current player
            zeroSum = sum(self.board[self.otherPlayer.side[0]:self.otherPlayer.side[-1] + 1])
            # print("\t", self.board[self.otherPlayer.side[0]:self.otherPlayer.side[-1] + 1])
            if zeroSum == 0:
                for seed in self.board:
                    self.otherPlayer.addBank(seed)

                for i in range(12): self.board[i] = 0
                self.endGame()
                break

            # ALGORITHM #9
            for idx in range(12):
                if idx in self.changedIdx:
                    changed_seed = self.board[idx]
                    if changed_seed == 4:
                        if idx in self.currentPlayer.getSide():
                            self.currentPlayer.addBank(4)
                            self.board[idx] = 0
                            continue
                        elif idx in self.otherPlayer.getSide():
                            self.otherPlayer.addBank(4)
                            self.board[idx] = 0
                            continue

            self.displayGame()
            self.dataObj.setBeads(self.board, [self.player1.bank, self.player2.bank])
            return self.dataObj.getBeads()

if __name__ == "__main__":
    g = Game()
    g.isValidMove((114, 166))
    print(g.dataObj.getBeads())
