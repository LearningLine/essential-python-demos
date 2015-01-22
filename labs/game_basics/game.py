
# 1. Print out cheesy welcome
print("Welcome to tic-tac-toe pro v1 lite, buy us at the app store")

# 2. setup game data structures
x = 1
o = -1
e = 0
game = [
    [e, e, e],
    [e, e, e],
    [e, e, e],
]

# 3. Print the empty board (will require two for loops)
#     Convert value of x => 'x'
#     Convert value of o => 'o'
#     Convert value of e (empty) => '.'
for row in game:     # get each row
    for cell in row: # get every cell from the row
        #print(cell)
        if cell == e:
            print('.', end=' ')
        elif cell == x:
            print('x', end=' ')
        elif cell == o:
            print('o', end=' ')
    print()


# 4. Setup game loop variables
# turn, winner, and hasWon.
turn = x
hasWon = False
winner = None


# 5. Game loop (while loop until someone has won):
while not hasWon:
#   print who's turn it is (X or O)
    print("It's " + ("x's" if turn == x else "y's") + " turn" )

#   ask user for row (via input('prompt text'), convert to int via int(text))
#   ask user for column (same)
    row = int( input("Which row do you play? ") )
    col = int( input("Which col do you play? ") )

#   verify row and column are in bounds
    if row < 0 or row > 2:
        print("bad row")
        continue

#   verify that entry is not already chosen
    play =game[row][col]
    if play != e:
        print("Sorry, that cell is played, try again")
        continue

    play = game[row][col]

#   set row/column to correct value (e.g. game[row][column] = x)
    game[row][col]= turn

#   show the board again (now that it's updated)
    for row in game:     # get each row
        for cell in row: # get every cell from the row
            #print(cell)
            if cell == e:
                print('.', end=' ')
            elif cell == x:
                print('x', end=' ')
            elif cell == o:
                print('o', end=' ')
        print()

#   check for a winner (any row or diagonal sums to 3 => x's win, -3 => o's win)
    g = game
    possible_wins = [
        # diagonals
        [ g[0][0],g[1][1],g[2][2] ],
        [ g[2][0],g[1][1],g[0][2] ],
        [ g[0][0],g[0][1],g[0][2] ]
        # and so on...
    ]

    for win in possible_wins:
        if sum(win) == 3 or sum(win) == -3:
            hasWon = True
            winner = turn

#   switch players, repeat.
    turn *= -1

# 6. Announce winner and show the winning board.
print("We have winner! {0} has won".format(
    "x" if winner == x else "o"
))