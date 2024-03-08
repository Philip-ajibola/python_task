from tic_tac_teo_with_computer.value import Value


class Player:
    def __init__(self, player_id: int, value: Value):
        self.__id = player_id
        self.__value = value

    def play(self, position, ticTacTo) -> None:
        ticTacTo.pickPosition(position, self.__value)

    def get_value(self) -> Value:
        return self.__value

    def get_id(self) -> int:
        return self.__id