#! /usr/bin/local/python3

from lab.game import Game

def print_welcome_message():
    print("Welcome to tic-tac-toe profession v0.1")
    print()

def print_current_player(turn):
    if turn == 1:
        print("It's X's turn.")
    else:
        print("It's O's turn.")


def query_placement_from_user():
    row = int(input("Choose row (zero based): "))
    col = int(input("Choose column (zero based): "))
    return row, col


def main():
    # Print out cheesy welcome
    print_welcome_message()

    game = Game()

    print("The board is set:")
    print(game)

    while not game.hasWinner:
        print_current_player(game.currentPlayer)

        row, col = query_placement_from_user()

        if game.cell_already_played(row, col):
            print("Sorry, that position is already occupied with a {0}!".format(game[row][col]))
            print("try again")
            print(game)
            print()
            continue

        # play the cell
        game.play_cell(row, col)

        print("Excellent choice:")
        print(game)

        print()

        # check for a winner
        print("We're checking for a winner...")
        if not game.hasWinner:
            print("No winner yet, keep going!")
            print()

        game.swap_players()


    # Announce winner and show the winning board.
    print("We have a winner! It's the " + game.find_winner() + "'s!")
    print("Way to win the day")
    print()
    print(game)


if __name__ == "__main__":
    main()