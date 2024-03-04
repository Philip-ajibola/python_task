import re


def collect_input_count_digit_and_sentence(user_input):
    digits = re.sub("[^0-9]", "", user_input)
    alpha = re.sub("[^a-zA-Z]", "", user_input)
    return f"LETTER {len(alpha)} DIGIT {len(digits)}"


def collect_input_count_digit_and_sentence_one(user_input):
    digits = re.sub("[^0-9]", "", user_input)
    alpha = re.sub("[^a-zA-Z]", "", user_input)
    my_dict = {'LETTER': len(alpha), "DIGIT": len(digits)}
    return my_dict


def collect_input_and_pick_Upper_case_letter_and_lower_case_letter(user_input):
    upper = re.sub("[^A-Z]", "", user_input)
    lower = re.sub("[^a-z]", "", user_input)
    my_dict = {'UPPER CASE': len(upper), "LOWER CASE": len(lower)}
    return my_dict

