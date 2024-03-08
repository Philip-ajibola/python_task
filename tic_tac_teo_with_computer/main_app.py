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
            print()
            print(tic_tac_toe)
            if tic_tac_toe.getWinner() != "":
                print(tic_tac_toe.getWinner())
                break
            if number < 4:
                TicTacToeApp.check_empty_box_for_player_two(tic_tac_toe)
                print()
                print(tic_tac_toe)
                if tic_tac_toe.getWinner() != "":
                    print(tic_tac_toe.getWinner())
                    break

    @staticmethod
    def collect_player_one_input(tic_tac_toe: TicTacTo):
        player1_input = int(input("Player one enter the box you want to fill "))
        tic_tac_toe.pickPosition(player1_input, tic_tac_toe.get_player()[0].get_value())

    @staticmethod
    def collect_player_two_input(tic_tac_toe: TicTacTo):
        player2_input = int(input("Player two enter the box you want to fill "))
        tic_tac_toe.pickPosition(player2_input, tic_tac_toe.get_player()[1].get_value())

    @staticmethod
    def check_empty_box_for_player_one(tic_tac_toe: TicTacTo):
        condition = True
        while condition:
            try:
                TicTacToeApp.collect_player_one_input(tic_tac_toe)
                condition = False
            except ValueError as e:
                print(e)

    @staticmethod
    def check_empty_box_for_player_two(tic_tac_toe: TicTacTo):
        condition = True
        while condition:
            try:
                TicTacToeApp.collect_player_two_input(tic_tac_toe)
                condition = False
            except ValueError as e:
                print(e)

    @staticmethod
    def main_menu(tic_tac_toe: TicTacTo):
        TicTacToeApp.display_heading()
        print()
        user_response = ""
        while user_response != "no":
            print(tic_tac_toe)
            TicTacToeApp.play(tic_tac_toe)
            user_response = input("Do you want to continue the game (yes or no) ").lower()
            if user_response == "no": break
            while user_response != "yes" and user_response != "no":
                user_response = input("Please enter 'yes' or not  :( ")
            tic_tac_toe = TicTacTo()
        print("THANK YOU FOR PLAYING TICTACTO GAME \n HOPE YOU ENJOYED PLAYING IT ")


if __name__ == "__main__":
    tic_tac_toe_game = TicTacTo()
    TicTacToeApp.main_menu(tic_tac_toe_game)
