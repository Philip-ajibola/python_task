def display_element_from_one_to_fifteen():
    list1 = []
    for number in range(1, 16):
        list1.append(number)
    return list1


def duplicate_all_element_in_first_function():
    list1 = []
    list2 = []
    for number in range(1, 16):
        list1.append(number)
        list2.append(number)
    list2 += list1
    return list2


def remove_duplicate_of_second_function():
    list1 = []
    for number in range(1, 16):
        list1.append(number)
    return list1


def add_every_third_element_in_list(list1):
    total = 0
    for number in list1[2::3]:
        total += number
    return total


def add_first_middle_last_number_in_list(list1):
    total = 0
    if len(list1) % 2 == 0:
        for number in range(len(list1)):
            if number != len(list1) / 2 and number == 0:
                total += list1[number]
                continue
            if number == len(list1) / 2:
                total += (list1[number] + list1[number -1]) / 2
                continue
            if number == len(list1)-1:
                total += list1[number]
        return total
    else:
        for number in list1[::len(list1)//2]:
            total += number
        return total


def collect_ten_numbers_from_user():
    list1 = []
    for number in range(11):
        userInput = eval(input("Enter number "))
        list.append(userInput)
    return list1

def return_collection_of_numbers_without_having_duplicate(list1):
    my_set = set(list1)
    return my_set


def sum_collection(my_set):
    if type(my_set)==set:
        total = 0
        for number in my_set:
            total += number
        return total
    else:
        return f"set type required not {type(my_set)}"


def find_interception(set1,set2):
    if type(set1) == set and type(set2)== set:
        set3 = set()
        for number in set1:
            if number in set2:
                set3.add(number)
        return set3
    else:
        return "both collection must be set"


