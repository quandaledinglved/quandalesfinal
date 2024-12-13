class TicTacToe:
    def __init__(self):
        # Initialize the game board as a 3x3 grid filled with spaces.
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        # Define the two players as "X" and "O".
        self.players = ["X", "O"]
        # Start with player 0 ("X").
        self.current_player = 0

    def print_board(self):
        # Print the current state of the board in a readable format.
        for row in self.board:
            print(" | ".join(row))  # Join cells in the row with vertical bars.
            print("-" * 9)  # Print a horizontal divider between rows.

    def check_winner(self):
        # Get the symbol of the current player ("X" or "O").
        player = self.players[self.current_player]
        
        # Check if any row is fully occupied by the current player's symbol.
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        # Check if any column is fully occupied by the current player's symbol.
        for col in range(3): 
            if all(row[col] == player for row in self.board):
                return True

        # Check the two diagonals for the current player's symbol.
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        # Return False if no winning condition is met.
        return False

    def is_full(self):
        # Check if all cells on the board are filled (no spaces left).
        return all(cell != " " for row in self.board for cell in row)

    def play(self):
        # Start the game loop and welcome the players.
        print("Welcome to Tic Tac Toe!")
        self.print_board()

        while True:
            # Announce the current player's turn.
            print(f"Player {self.players[self.current_player]}'s turn.")

            while True:
                try:
                    # Prompt the player to input their move as "row,col".
                    move = input("Enter your move (row and column as 'row,col'): ")
                    # Parse the input into row and column indices.
                    row, col = map(int, move.split(","))
                    # Check if the chosen cell is empty.
                    if self.board[row][col] == " ":
                        # Place the current player's symbol in the cell.
                        self.board[row][col] = self.players[self.current_player]
                        break
                    else:
                        print("This spot is already taken. Try again.")
                except (ValueError, IndexError):
                    # Handle invalid input and provide guidance to the player.
                    print("Invalid input. Make sure to enter row and column as numbers between 0 and 2, separated by a comma.")

            # Print the updated board state.
            self.print_board()

            # Check if the current player has won the game.
            if self.check_winner():
                print(f"Player {self.players[self.current_player]} wins!")
                break

            # Check if the board is full and the game is a draw.
            if self.is_full():
                print("It's a draw!")
                break

            # Switch to the other player for the next turn.
            self.current_player = 1 - self.current_player

if __name__ == "__main__":
    # Create an instance of the TicTacToe class and start the game.
    game = TicTacToe()
    game.play()
