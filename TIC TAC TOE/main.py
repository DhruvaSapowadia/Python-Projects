# import turtle
#
# screen = turtle.Screen()
# screen.setup(700, 700)
# screen.title("Tic Tac Toe")
# screen.setworldcoordinates(-5, -5, 5, 5)
# screen.bgcolor('light gray')
# screen.tracer(0, 0)
# turtle.hideturtle()
#
#
# def draw_board():
#     turtle.pencolor('green')
#     turtle.pensize(10)
#     turtle.up()
#     turtle.goto(-3, -1)
#     turtle.seth(0)
#     turtle.down()
#     turtle.fd(6)
#     turtle.up()
#     turtle.goto(-3, 1)
#     turtle.seth(0)
#     turtle.down()
#     turtle.fd(6)
#     turtle.up()
#     turtle.goto(-1, -3)
#     turtle.seth(90)
#     turtle.down()
#     turtle.fd(6)
#     turtle.up()
#     turtle.goto(1, -3)
#     turtle.seth(90)
#     turtle.down()
#     turtle.fd(6)
#
#
# def draw_circle(x, y):
#     turtle.up()
#     turtle.goto(x, y - 0.75)
#     turtle.seth(0)
#     turtle.color('red')
#     turtle.down()
#     turtle.circle(0.75, steps=100)
#
#
# def draw_x(x, y):
#     turtle.color('blue')
#     turtle.up()
#     turtle.goto(x - 0.75, y - 0.75)
#     turtle.down()
#     turtle.goto(x + 0.75, y + 0.75)
#     turtle.up()
#     turtle.goto(x - 0.75, y + 0.75)
#     turtle.down()
#     turtle.goto(x + 0.75, y - 0.75)
#
#
# def draw_piece(i, j, p):
#     if p == 0: return
#     x, y = 2 * (j - 1), -2 * (i - 1)
#     if p == 1:
#         draw_x(x, y)
#     else:
#         draw_circle(x, y)
#
#
# def draw(b):
#     draw_board()
#     for i in range(3):
#         for j in range(3):
#             draw_piece(i, j, b[i][j])
#     screen.update()
#
#
# # return 1 if player 1 wins, 2 if player 2 wins, 3 if tie, 0 if game is not over
# def gameover(b):
#     if b[0][0] > 0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]: return b[0][0]
#     if b[1][0] > 0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]: return b[1][0]
#     if b[2][0] > 0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]: return b[2][0]
#     if b[0][0] > 0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]: return b[0][0]
#     if b[0][1] > 0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]: return b[0][1]
#     if b[0][2] > 0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]: return b[0][2]
#     if b[0][0] > 0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]: return b[0][0]
#     if b[2][0] > 0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]: return b[2][0]
#     p = 0
#     for i in range(3):
#         for j in range(3):
#             p += (1 if b[i][j] > 0 else 0)
#     if p == 9:
#         return 3
#     else:
#         return 0
#
#
# def play(x, y):
#     global turn
#     i = 3 - int(y + 5) // 2
#     j = int(x + 5) // 2 - 1
#     if i > 2 or j > 2 or i < 0 or j < 0 or b[i][j] != 0: return
#     if turn == 'x':
#         b[i][j], turn = 1, 'o'
#     else:
#         b[i][j], turn = 2, 'x'
#     draw(b)
#     r = gameover(b)
#     if r == 1:
#         screen.textinput("Game over!", "X won!")
#     elif r == 2:
#         screen.textinput("Game over!", "O won!")
#     elif r == 3:
#         screen.textinput("Game over!", "Tie!")
#
#
# b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# draw(b)
# turn = 'x'
# screen.onclick(play)
# turtle.mainloop()


import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
