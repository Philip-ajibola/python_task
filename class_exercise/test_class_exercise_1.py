from unittest import TestCase

from class_exercise import class_exercise_1


class Test(TestCase):
    def test_collect_input_count_digit_and_sentence(self):
        user_input = 'Hello World! 123'
        result = class_exercise_1.collect_input_count_digit_and_sentence(user_input)
        expected_result = 'LETTER 10 DIGIT 3'
        self.assertEqual(result,expected_result)

    def test_collect_input_count_digit_and_sentence_one(self):
        user_input = 'Hello World! 123'
        result = class_exercise_1.collect_input_count_digit_and_sentence_one(user_input)
        expected_result = {"LETTER":10,"DIGIT":3,}
        self.assertEqual(result,expected_result)

    def test_collect_input_and_pick_alphabet_letter(self):
        user_input = 'Hello World!'
        result = class_exercise_1.collect_input_and_pick_Upper_case_letter_and_lower_case_letter(user_input)
        expected_result = {"UPPER CASE":2,"LOWER CASE":8}
        self.assertEqual(expected_result,result)