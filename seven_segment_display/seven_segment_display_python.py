def display_seven_segment_of(binary_number):
    __check_length_of(binary_number)
    __check_every_character_of_the_input(binary_number)
    condition = is_the_last_char_1(binary_number[-1])
    if condition:
        __display_segment(binary_number)


def __display_segment(binary_number):
    bool_list = __convert_input_to_boolean_list(binary_number)
    __display_horizontal(bool_list[0])
    __display_vertical(bool_list[5], bool_list[1])
    __display_horizontal(bool_list[6])
    __display_vertical(bool_list[4], bool_list[2])
    __display_horizontal(bool_list[3])


def __check_every_character_of_the_input(user_input: str):
    for character in user_input:
        if character != "1" and character != "0": raise ValueError("Binary Number Expected 0's and 1's")


def __display_horizontal(condition: bool):
    if condition: print(" # # # # #")


def __display_vertical(condition1: bool, condition2: bool):
    if condition1 and condition2:
        for numb in range(4):
            print("#         #")
    if condition1 is False and condition2 is True:
        for numb in range(4):
            print("         #")
    if condition1 is True and condition2 is False:
        for numb in range(4):
            print("#         ")


def __convert_input_to_boolean_list(binary_number: str) -> []:
    list_char = []
    list_char += binary_number
    bool_list = []
    for character in list_char:
        bool_list.append(character == "1")
    return bool_list


def __check_length_of(user_input: str):
    if len(user_input) != 8: raise ValueError("Invalid Input ")


def is_the_last_char_1(last_char: str) -> bool:
    return last_char == "1"


condition = True
while condition:
    try:
        number = input("Enter binary")
        display_seven_segment_of(number)
        condition = False
    except Exception as e:
        print(e)
        number = input("Enter binary")
        display_seven_segment_of(number)
        condition = False
