from tic_tac_teo_with_computer.player import Player
from tic_tac_teo_with_computer.value import Value


class TicTacToe:
    def __init__(self):
        value = Value.EMPTY
        self.board = [[value, value, value], [value, value, value], [value, value, value]]
        self.players = []
        self.checker = 0
        self.box_checker = []
        player1 = Player(1, Value.X)
        player2 = Player(2, Value.O)
        self.players.append(player1)
        self.players.append(player2)

    def get_board(self):
        return self.board

    def get_player(self):
        return self.players

    def pickPosition(self, position: int, value: Value):
        self.__validate_user_input(position)
        self.fill_box(position, value)
        self.checker += 1

    def __check_if_player_played_in_row_one_and_fill_board(self, position: int, value: Value):
        if 0 < position <= 3:
            if position == 1:
                self.board[0][0] = value
            elif position == 2:
                self.board[0][1] = value
            else:
                self.board[0][2] = value

    def __check_if_player_played_in_row_two_and_fill_board(self, position: int, value: Value):
        if 3 < position <= 6:
            if position == 4:
                self.board[1][0] = value
            elif position == 5:
                self.board[1][1] = value
            else:
                self.board[1][2] = value

    def __check_if_player_played_in_row_three_and_fill_board(self, position: int, value: Value):
        if 6 < position <= 9:
            if position == 7:
                self.board[2][0] = value
            elif position == 8:
                self.board[2][1] = value
            else:
                self.board[2][2] = value

    @staticmethod
    def __validate_user_input(user_input: int):
        if user_input > 9 or user_input <= 0:
            raise ValueError("Box Number not found")

    def __check_if_box_is_empty(self, position: int):
        if self.box_checker.__contains__(position):
            raise ValueError("Box not empty")
        self.box_checker.append(position)

    def getWinner(self):
        winner = ""
        if self.__check_if_player_win_by_row() is not None:
            winner = self.__check_if_player_win_by_row()
        elif self.__check_if_player_win_by_column() is not None:
            winner = self.__check_if_player_win_by_column()
        elif self.__check_if_player_win_diagonally() is not None:
            winner = self.__check_if_player_win_diagonally()
        elif self.checker == 9:
            winner = "The game is a draw"
        return winner

    def __check_if_player_win_by_row(self) -> str:
        for number in range(len(self.board[0])):
            if self.board[number][0] == self.board[number][1] and self.board[number][0] == self.board[number][2] and \
                    self.board[number][0] != Value.EMPTY:
                return self.__check_winner_with_players_values(self.board[number][0])

    def __check_if_player_win_by_column(self) -> str:
        for number in range(len(self.board[0])):
            if self.board[0][number] == self.board[1][number] and self.board[0][number] == self.board[2][number] and \
                    self.board[0][number] != Value.EMPTY:
                return self.__check_winner_with_players_values(self.board[0][number])

    def __check_winner_with_players_values(self, value: Value) -> str:
        if value == Value.X:
            return "Congratulations\nYou Won The Computer"
        elif value == Value.O:
            return "The Computer Wins"

    def __check_if_player_win_diagonally(self) -> str:
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] != Value.EMPTY:
            return self.__check_winner_with_players_values(self.board[0][0])
        elif self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0] and self.board[0][2] != Value.EMPTY:
            return self.__check_winner_with_players_values(self.board[0][2])

    def fill_box(self, position: int, value: Value) -> None:
        self.__check_if_box_is_empty(position)
        self.__check_if_player_played_in_row_one_and_fill_board(position, value)
        self.__check_if_player_played_in_row_two_and_fill_board(position, value)
        self.__check_if_player_played_in_row_three_and_fill_board(position, value)

    def __str__(self):
        return f"{self.display_board()}"

    def display_board(self):
        expectedString = ""
        for row in self.board:
            for cell in row:
                expectedString += self.__printSpaceIfValueIsOorX(cell) + " |"
            expectedString += "\n______________________\n"
        return expectedString

    @staticmethod
    def __printSpaceIfValueIsOorX(value: Value):
        if value == Value.X or value == Value.O:
            return "  " + value.name + "  "
        else:
            return Value.EMPTY.name
