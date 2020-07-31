from random import randint

# create and populate the board
board = []

for x in range(5):
    board.append(["O"] * 5)

# convert the board to space delimited and print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

# create the battleship X and Y axis positions randomly
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print("Ship row:)"+str(ship_row)
#print("Ship col:)"+str(ship_col)

# ask the user for a guess for X and Y axis
for turn in range(4):
    print("Turn ", turn+1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    # check if hit/miss/off the board/previous guess
    if guess_row == ship_row and guess_col == ship_col: # hit
        print("\nCongratulations! You sank my battleship!")
        break # end the for loop
    elif guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4:
        print("\nOops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
        print("\nYou guessed that one already.")
    else:
        print("\nYou missed my battleship!") # miss
        board[guess_row][guess_col] = "X"
 
    print_board(board)

    # inform user that they are out of moves
    if turn == 3:
        print("\nGame Over")