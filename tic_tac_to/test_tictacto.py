from unittest import TestCase

from tic_tac_to.tictacto import TicTacTo
from tic_tac_to.value import Value


class TestTicTacTo(TestCase):
    def setUp(self):
        self.ticTacto = TicTacTo()
        self.players = self.ticTacto.get_player()

    def test_that_game_has_a_marking_board(self):
        expected = self.ticTacto.get_board()
        board = [[Value.EMPTY, Value.EMPTY, Value.EMPTY], [Value.EMPTY, Value.EMPTY, Value.EMPTY],
                 [Value.EMPTY, Value.EMPTY, Value.EMPTY]]
        self.assertEqual(expected, board)

    def test_that_game_has_two_players(self):
        self.assertEqual(2, len(self.players))

    def test_that_player_can_play_game_and_fill_board(self):
        self.players[0].play(1, self.ticTacto)
        self.assertEqual(Value.X, self.players[0].get_value())

    def test_that_player_one_has_a_unique_value(self):
        self.assertEqual(Value.X, self.players[0].get_value())

    def test_that_player_two_has_a_unique_value(self):
        self.assertEqual(Value.O, self.players[1].get_value())

    def test_that_player_one_has_a_unique_id(self):
        self.assertEqual(1, self.players[0].get_id())

    def test_that_player_two_has_a_unique_id(self):
        self.assertEqual(2, self.players[1].get_id())

    def test_that_row_one_can_be_filled(self):
        self.players[0].play(1, self.ticTacto)
        self.players[1].play(2, self.ticTacto)
        self.players[0].play(3, self.ticTacto)
        expected = [Value.X, Value.O, Value.X]
        self.assertEqual(expected, self.ticTacto.get_board()[0])

    def test_that_row_two_can_be_filled(self):
        self.players[0].play(4, self.ticTacto)
        self.players[1].play(5, self.ticTacto)
        self.players[0].play(6, self.ticTacto)
        expected = [Value.X, Value.O, Value.X]
        self.assertEqual(expected, self.ticTacto.get_board()[1])

    def test_that_row_three_can_be_filled(self):
        self.players[0].play(7, self.ticTacto)
        self.players[1].play(8, self.ticTacto)
        self.players[0].play(9, self.ticTacto)
        expected = [Value.X, Value.O, Value.X]
        self.assertEqual(expected, self.ticTacto.get_board()[2])

    def test_that_when_number_greater_than_9_is_entered_error_message_is_thrown(self):
        self.players[0].play(7, self.ticTacto)
        self.players[1].play(8, self.ticTacto)
        with self.assertRaises(ValueError):
            self.players[0].play(7, self.ticTacto)

    def test_that_when_Player_try_to_play_in_an_already_filled_box_error_is_thrown(self):
        with self.assertRaises(ValueError):
            self.players[0].play(10, self.ticTacto)