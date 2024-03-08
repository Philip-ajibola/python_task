import time
from random import randint

from tic_tac_teo_with_computer.tic_tac_teo import TicTacToe


class TicTacToeApp:
    list1 = []

    @staticmethod
    def display_heading():
        print(""""
        Welcome to Tic-Tac-Toe Game 
        Enjoy your game as you play
        You Are Playing With The Computer

        Your Value Is X While The Computer Value is O 
        
                Enjoy Your Game With The Computer
        """)

    @staticmethod
    def play(tic_tac_toe: TicTacToe):
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
        TicTacToeApp.list1.clear()

    @staticmethod
    def collect_player_one_input(tic_tac_toe: TicTacToe):
        player1_input = int(input("Player one enter the box you want to fill "))
        TicTacToeApp.list1.append(player1_input)
        tic_tac_toe.pickPosition(player1_input, tic_tac_toe.get_player()[0].get_value())

    @staticmethod
    def collect_player_two_input(tic_tac_toe: TicTacToe):
        print("The Computer is Playing Next... ")
        time.sleep(1)
        computer_input = randint(1, 9)
        while TicTacToeApp.list1.__contains__(computer_input):
            print("yes")
            computer_input = randint(1, 9)
        TicTacToeApp.list1.append(computer_input)
        tic_tac_toe.pickPosition(computer_input, tic_tac_toe.get_player()[1].get_value())

    @staticmethod
    def check_empty_box_for_player_one(tic_tac_toe: TicTacToe):
        condition = True
        while condition:
            try:
                TicTacToeApp.collect_player_one_input(tic_tac_toe)
                condition = False
            except ValueError as e:
                print(e)

    @staticmethod
    def check_empty_box_for_player_two(tic_tac_toe: TicTacToe):
        condition = True
        while condition:
            try:
                TicTacToeApp.collect_player_two_input(tic_tac_toe)
                condition = False
            except ValueError as e:
                print(e)

    @staticmethod
    def main_menu(tic_tac_toe: TicTacToe):
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
            tic_tac_toe = TicTacToe()
        print("\nTHANK YOU FOR PLAYING TICTACTO GAME \n HOPE YOU ENJOYED PLAYING IT ")


if __name__ == "__main__":
    tic_tac_toe_game = TicTacToe()
    TicTacToeApp.main_menu(tic_tac_toe_game)
