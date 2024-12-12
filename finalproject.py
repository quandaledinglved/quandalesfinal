class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.current_player = 0

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def check_winner(self):
        player = self.players[self.current_player]
    
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        for col in range(3): 
            if all(row[col] == player for row in self.board):
                return True

        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.print_board()

        while True:
            print(f"Player {self.players[self.current_player]}'s turn.")

            while True:
                try:
                    move = input("Enter your move (row and column as 'row,col'): ")
                    row, col = map(int, move.split(","))
                    if self.board[row][col] == " ":
                        self.board[row][col] = self.players[self.current_player]
                        break
                    else:
                        print("This spot is already taken. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Make sure to enter row and column as numbers between 0 and 2, separated by a comma.")

            self.print_board()

            if self.check_winner():
                print(f"Player {self.players[self.current_player]} wins!")
                break

            if self.is_full():
                print("It's a draw!")
                break

            self.current_player = 1 - self.current_player

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
