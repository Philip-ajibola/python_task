from dataclasses import dataclass

#from tic_tac_to.tictacto import TicTacTo
from tic_tac_to.value import Value


@dataclass
class Player:
    def __init__(self, player_id: int, value: Value):
        self.id = id
        self.value = value

    def play(self, position, ticTacTo) -> None:
        ticTacTo.pickPosition(position, self.value)

    def get_value(self) -> Value:
        return self.value
