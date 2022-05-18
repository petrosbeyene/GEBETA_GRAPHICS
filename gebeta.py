"""Gebeta

Traditional Ethiopian Game.
"""

# Import necessary modules
import random

def main():
    """Main entry of the program."""

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
    
    for idx in range(12):
        playing_board.insert(idx, 4)    

    for idx2 in range(6):
        upside_idx.insert(idx2, idx2)
        downside_idx.insert(idx2 + 6, idx2 + 6)

    while True:
        # Show The Game
        print(playing_board[0:6])
        print(playing_board[6:12])
        print("Bank1:",players[0] [0],"\tBank2:",players[1] [0])
        print("Current Player:","Player"+str(current_player+1))

        inp = int(input("Choose a pit from 1 to 12: "))
        
        if inp in upside_idx:
            players [current_player].insert(1, upside_idx)
            players [1 - current_player].insert(1, downside_idx)
        elif inp in downside_idx:
            players [current_player].insert(1, downside_idx)
            players [1 - current_player].insert(1, upside_idx)
    
        start_seed = inp
        end_seed = start_seed + playing_board[inp - 1]
        playing_board[inp - 1] = 0
        changed_idx.append(inp)
        # print(start_seed, end_seed) # debugger line

        for seed in range(start_seed, end_seed):
            if seed > 11:
                seed = seed % 12
            changed_idx.append(seed)
            playing_board[seed] = playing_board[seed] + 1
        
        if playing_board[end_seed] == 1:
            current_player = 1 - current_player
            continue
        if playing_board[end_seed] == 4:
            pass

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
                break
        elif sideZero == 6 and asideZero < 6:
            for seed in playing_board:
                players[1 - current_player] [0] += seed
                break

        # ALGORITHM #7
        for idx in range(12):
            if idx in changed_idx:
                changed_seed = playing_board[idx]
                if changed_seed == 4:
                    if idx in players[current_player][1]:
                        players[current_player][0] += 4
                        playing_board[idx] = 0
                        current_player = 1 - current_player
                        continue
                    elif idx in players[1 - current_player][1]:
                        players[1 - current_player][0] += 4
                        playing_board[idx] = 0
                        current_player = 1 - current_player
                        continue
        
        # give the turn to the other player
        current_player = 1 - current_player
        
main()
