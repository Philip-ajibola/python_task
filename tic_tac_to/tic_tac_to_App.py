from tic_tac_to.tictacto import TicTacTo


class TicTacToeApp:
    @staticmethod
    def display_heading():
        print(""""
        Welcome to Tic-Tac-Toe Game 
        Enjoy your game as you play
        
        Player One Uses X and Player Two Uses O
        
        """)

    @staticmethod
    def play(tic_tac_toe: TicTacTo):
        for number in range(5):
            TicTacToeApp.check_empty_box_for_player_one(tic_tac_toe)
            print(tic_tac_toe)
            if tic_tac_toe.getWinner() is not None:
                print(tic_tac_toe.getWinner())
                break
            if number < 4:
                TicTacToeApp.check_empty_box_for_player_two(tic_tac_toe)
                print(tic_tac_toe)
                if tic_tac_toe.getWinner() is not None:
                    print(tic_tac_toe.getWinner())
                    break

    @staticmethod
    def collect_player_one_input(tic_tac_toe: TicTacTo):
        player1_input = int(input("Player one enter the box you want to fill "))
        tic_tac_toe.fill_box(player1_input, tic_tac_toe.get_player()[0].get_value())

    @staticmethod
    def collect_player_two_input(tic_tac_toe: TicTacTo):
        player2_input = int(input("Player one enter the box you want to fill "))
        tic_tac_toe.fill_box(player2_input, tic_tac_toe.get_player()[1].get_value())

    @staticmethod
    def check_empty_box_for_player_one(tic_tac_toe: TicTacTo):
        condition = True
        while condition:
            try:
                TicTacToeApp.collect_player_one_input(tic_tac_toe)
                condition = False
            except Exception as e:
                print(e)

    @staticmethod
    def check_empty_box_for_player_two(tic_tac_toe: TicTacTo):
        condition = True
        while condition:
            try:
                TicTacToeApp.collect_player_two_input(tic_tac_toe)
                condition = False
            except Exception as e:
                print(e)

    @staticmethod
    def main_menu(tic_tac_toe:TicTacTo):
        TicTacToeApp.display_heading()
        print()
        user_response = ""
        while user_response is not "no":
            print(tic_tac_toe)
            TicTacToeApp.play(tic_tac_toe)
