import copy

class Othello:
    def __init__(self):
        self.board_size = 8
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.board[int(self.board_size/2)-1][int(self.board_size/2)-1] = 'O'
        self.board[int(self.board_size/2)-1][int(self.board_size/2)] = 'X'
        self.board[int(self.board_size/2)][int(self.board_size/2)-1] = 'X'
        self.board[int(self.board_size/2)][int(self.board_size/2)] = 'O'
        self.current_player = 'X'

    def display_board(self):
        print("   0 1 2 3 4 5 6 7")
        print("  ----------------")
        for i in range(self.board_size):
            print(f"{i}|", end=" ")
            for j in range(self.board_size):
                print(self.board[i][j], end=" ")
            print()

    def is_valid_move(self, row, col):
        return 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == ' '

    def is_valid_direction(self, row, col, direction):
        dr, dc = direction
        r, c = row + dr, col + dc

        if not (0 <= r < self.board_size and 0 <= c < self.board_size) or self.board[r][c] != self.get_opponent():
            return False

        r += dr
        c += dc

        while 0 <= r < self.board_size and 0 <= c < self.board_size:
            if self.board[r][c] == self.current_player:
                return True
            elif self.board[r][c] == ' ':
                return False
            r += dr
            c += dc

        return False

    def get_opponent(self):
        return 'O' if self.current_player == 'X' else 'X'

    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return False

        self.board[row][col] = self.current_player

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for direction in directions:
            if self.is_valid_direction(row, col, direction):
                self.flip_tiles(row, col, direction)

        self.current_player = self.get_opponent()
        return True

    def flip_tiles(self, row, col, direction):
        dr, dc = direction
        r, c = row + dr, col + dc

        while self.board[r][c] == self.get_opponent():
            self.board[r][c] = self.current_player
            r += dr
            c += dc

    def get_score(self):
        x_score = sum(row.count('X') for row in self.board)
        o_score = sum(row.count('O') for row in self.board)
        return {'X': x_score, 'O': o_score}

    def game_over(self):
        return all(' ' not in row for row in self.board) or (self.get_score()['X'] == 0) or (self.get_score()['O'] == 0)

    def get_winner(self):
        score = self.get_score()
        if score['X'] > score['O']:
            return 'X'
        elif score['O'] > score['X']:
            return 'O'
        else:
            return 'Tie'

    def play_two_players(self):
        while not self.game_over():
            self.display_board()
            print(f"Current Score - X: {self.get_score()['X']}, O: {self.get_score()['O']}")

            row, col = map(int, input(f"Player {self.current_player}, enter your move (row and column, separated by a space): ").split())
            
            if not self.make_move(row, col):
                print("Invalid move. Try again.")
            else:
                self.display_board()

        winner = self.get_winner()
        print("Game Over!")
        self.display_board()
        print(f"The winner is: {winner}")

# Example usage:
othello_game = Othello()
othello_game.play_two_players()
