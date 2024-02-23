import unittest
import task_two


class MyTestCase(unittest.TestCase):
    def test_that_function_add_even_and_odd_numbers_in_range_number(self):
        number = 15
        list1 = task_two.sum_even_and_odd_number(number)
        self.assertEqual(49,list1[1])
        self.assertEqual(56, list1[0])

    def test_that_function_add_even_and_odd_numbers_in_range_number_two(self):
        number = 15
        result = "sum of even number is 56 sum of odd numbers is 49"

        self.assertEqual(result, task_two.sum_even_and_odd_number_one(15))



