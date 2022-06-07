"""Gebeta

Traditional Ethiopian Game.
"""

# Import necessary modules
import random

current_player = round(random.random())
bank1 = 0
bank2 = 0
player1 = [bank1,]
player2 = [bank2,]
players = [player1, player2]
changed_idx = list()
playing_board = list()
upside_idx = list()
downside_idx = list()

def displayGame():
    """A function to display the game"""
    print(playing_board[0:6])
    print(playing_board[6:12])
    print("Current Player: Player{}".format(current_player + 1), end = "\t")
    print("\tBank1:",players[0][0],"\tBank2:",players[1][0])

def initBoard():
    """A function to initialize the playing board."""
    for idx in range(12):
        playing_board.insert(idx, 4)    

    for idx2 in range(6):
        upside_idx.insert(idx2, idx2)
        downside_idx.insert(idx2 + 6, idx2 + 6)

def endGame():
    """A function to mark the end of the game."""
    pass

def main():
    """Main entry of the program."""
    global current_player
    initBoard()
    print("Starting Player:","Player"+str(current_player + 1))
    displayGame()
    
    inp = int(input("Choose a pit from 1 to 12: "))
    
    if inp in upside_idx:
        players [current_player].insert(1, upside_idx)
        players [1 - current_player].insert(1, downside_idx)
    elif inp in downside_idx:
        players [current_player].insert(1, downside_idx)
        players [1 - current_player].insert(1, upside_idx)
    
    # Game loop
    while True:
        if inp not in players[current_player][1]:
            inp = int(input("Player{} - choose a pit again: ".format(current_player + 1)))
            continue

        start_seed = inp - 1

        # Seeding loop 
        while True:
            end_seed = start_seed + playing_board[start_seed]
            playing_board[start_seed] = 0
            changed_idx.append(start_seed)
            
            # print(start_seed, end_seed) # debugger line
            
            for seed_idx in range(start_seed + 1, end_seed + 1):
                if seed_idx > 11:
                    seed_idx = seed_idx % 12
                changed_idx.append(seed_idx)
                playing_board[seed_idx] = playing_board[seed_idx] + 1
                
            # Debugger lines - to see each step
            print(playing_board[0:6])
            print(playing_board[6:12])
            print()

            if playing_board[seed_idx] == 1:
                current_player = 1 - current_player
                break
            elif playing_board[seed_idx] == 4:
                if seed_idx in players[current_player][1]:
                    players[current_player][0] += 4
                    current_player = 1 - current_player
                elif seed_idx in players[1 - current_player][1]:
                    players[1 - current_player][0] += 4
                    current_player = 1 - current_player
                break
            elif playing_board[seed_idx] != 4 and playing_board[start_seed] != 1:
                start_seed = seed_idx
                continue
        
        # Check the end of the game
        sideZero = 0
        asideZero = 0
        for idx in players[current_player][1]:
            if playing_board[idx] == 0:
                sideZero += 1
        for idx in players[1 - current_player][1]:
            if playing_board[idx] == 0:
                asideZero += 1
        if asideZero == 6 and sideZero < 6:
            for seed in playing_board:
                players[current_player][0] += seed
                endGame()
                break
        elif sideZero == 6 and asideZero < 6:
            for seed in playing_board:
                players[1 - current_player] [0] += seed
                endGame()
                break

        # ALGORITHM #9
        for idx in range(12):
            if idx in changed_idx:
                changed_seed = playing_board[idx]
                if changed_seed == 4:
                    if idx in players[current_player][1]:
                        players[current_player][0] += 4
                        playing_board[idx] = 0
                        continue
                    elif idx in players[1 - current_player][1]:
                        players[1 - current_player][0] += 4
                        playing_board[idx] = 0
                        continue

        displayGame()
        inp = int(input("Player{} - choose a pit from {} to {}: "
            .format(current_player + 1, players[current_player][1][0] + 1, players[current_player][1][-1] + 1)))

main()
