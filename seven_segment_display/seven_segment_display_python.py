def display_seven_segment_of(binary_number):
    list_char = []
    list_char += binary_number
    bool_list = []
    for character in list_char:
        bool_list.append(character == "1")


def display_horizontal(condition):
    if condition: print(" # # # # #")


def display_vertical(condition1, condition2):
    if condition1 and condition2: print(" #         #")
    if condition1 is False and condition2 is True: print("         #")
    if condition1 is True and condition2 is False: print("         #")


number = "11111111"
display_seven_segment_of(number)
