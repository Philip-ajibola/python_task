from unittest import TestCase

from tic_tac_to.tictacto import TicTacTo
from tic_tac_to.value import Value


class TestTicTacTo(TestCase):
    def setUp(self):
        self.ticTacto = TicTacTo()

    def test_that_game_has_a_marking_board(self):
        expected = self.ticTacto.get_board()
        board = [[Value.EMPTY, Value.EMPTY, Value.EMPTY], [Value.EMPTY, Value.EMPTY, Value.EMPTY],
                 [Value.EMPTY, Value.EMPTY, Value.EMPTY]]
        self.assertEqual(expected, board)

    def test_that_game_has_two_players(self):
        players = self.ticTacto.get_player()
        self.assertEqual(2, len(players))

    def test_that_player_can_play_game_and_fill_board(self):
        players = self.ticTacto.get_player()
        players[0].play(1, self.ticTacto)
        self.assertEqual(Value.X, players[0].get_value())

    def test_that_player_one_has_a_unique_value(self):
        players = self.ticTacto.get_player()
        self.assertEqual(Value.X, players[0].get_value())

    def test_that_player_two_has_a_unique_value(self):
        players = self.ticTacto.get_player()
        self.assertEqual(Value.O, players[1].get_value())

    def test_that_player_one_has_a_unique_id(self):
        players = self.ticTacto.get_player()
        self.assertEqual(1, players[0].get_id())

    def test_that_player_two_has_a_unique_id(self):
        players = self.ticTacto.get_player()
        self.assertEqual(2, players[1].get_id())
