# Algorithm
1. Define a *playing board* as an array of twelve integer varibales (or *pits*) initially containing a value of four before the start of the game.
2. Define two variables called *bank1* and *bank2* initially containig a zero value. 
3. Define two players as an array of two variables, one is the bank and the other is the side.
4. Define an array of players containing the two players.
5. Randomly assign the starting player.
## INFINITE LOOP - Game loop
6. Prompt the starting player to choose a pit to be seeded.
7. Map the sides of the board to players wrt step 6.
## INFINITE LOOP - Seeding loop
8. Player selects a pit and starts adding (seeding) the total numbers (or *seeds*) one at a time in a clockwise direction to other consecutive pits until it terminates due to one or many of the following conditions:
    1. All the pits containing positive numbers end up all on the other player's side. This condition also marks the end of the game.
    2. The terminating pit after one iteration contains zero value before seeding, i.e. now 1 after seeding.
    3. The terminating pit after one iteration contains exactly a value of four. In this case:
        1. If the terminating pit is on the side of the current player, increminate the bank of the player by four and give the turn to the other player.
        2. Or other wise, if the pit is on the side of the other player, also increminate the bank of this player by four but the player will take the turn to him self.
9. Through out the game if any of the pits end up containing exactly a value of four after one iteration of the game, the pits will be added to the bank of a player wrt the side they exist. 
10. After the end of the game if the value of the banks of both players is the same the game restarts with a draw.
11. The winner will be the one containing more seeds in his/her bank at the end of the game.
