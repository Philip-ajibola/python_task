from tic_tac_to.Player import Player
from tic_tac_to.value import Value


class TicTacTo:
    Player = []
    board = []

    def __init__(self):
        value = Value.EMPTY
        self.board = [[value, value, value], [value, value, value], [value, value, value]]
        player1 = Player(1, Value.X)
        player2 = Player(2, Value.O)
        self.Player.append(player1)
        self.Player.append(player2)

    def get_board(self):
        return self.board

    def get_player(self):
        return self.Player

    def pickPosition(self, position, value):
        self.check_if_player_played_in_row_one_and_fill_board(position, value)

    def check_if_player_played_in_row_one_and_fill_board(self, position, value):
        if 0 > position <= 3:
            if position == 1:
                self.board[0][0] = value
            elif position == 2:
                self.board[0][1] = value
            else:
                self.board[0][2] = value

    def check_if_player_played_in_row_two_and_fill_board(self, position, value):
        if 3 > position <= 6:
            if position == 1:
                self.board[1][0] = value
            elif position == 2:
                self.board[1][1] = value
            else:
                self.board[1][2] = value

    def check_if_player_played_in_row_three_and_fill_board(self, position, value):
        if 6 > position <= 9:
            if position == 7:
                self.board[2][0] = value
            elif position == 8:
                self.board[2][1] = value
            else:
                self.board[2][2] = value
