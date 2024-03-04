from tic_tac_to.Player import Player
from tic_tac_to.value import Value


class TicTacTo:
    board = []

    def __init__(self):
        value = Value.EMPTY
        self.board = [[value, value, value], [value, value, value], [value, value, value]]
        self.players = []
        self.box_checker = {}
        player1 = Player(1, Value.X)
        player2 = Player(2, Value.O)
        self.players.append(player1)
        self.players.append(player2)

    def get_board(self):
        return self.board

    def get_player(self):
        return self.players

    def pickPosition(self, position: int, value: Value):
        self.validate_user_input(position)
        self.check_if_box_is_empty(position)
        self.check_if_player_played_in_row_one_and_fill_board(position, value)
        self.check_if_player_played_in_row_two_and_fill_board(position, value)
        self.check_if_player_played_in_row_three_and_fill_board(position, value)

    def check_if_player_played_in_row_one_and_fill_board(self, position: int, value: Value):
        if 0 < position <= 3:
            if position == 1:
                self.board[0][0] = value
            elif position == 2:
                self.board[0][1] = value
            else:
                self.board[0][2] = value

    def check_if_player_played_in_row_two_and_fill_board(self, position: int, value: Value):
        if 3 < position <= 6:
            if position == 4:
                self.board[1][0] = value
            elif position == 5:
                self.board[1][1] = value
            else:
                self.board[1][2] = value

    def check_if_player_played_in_row_three_and_fill_board(self, position: int, value: Value):
        if 6 < position <= 9:
            if position == 7:
                self.board[2][0] = value
            elif position == 8:
                self.board[2][1] = value
            else:
                self.board[2][2] = value

    def validate_user_input(self, user_input: int):
        if user_input > 9: raise ValueError("Box Number not found")

    def check_if_box_is_empty(self, position: int):
        condition = self.box_checker.add(position)
        if not condition:
            raise ValueError("Box not empty")
