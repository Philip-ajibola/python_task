from unittest import TestCase
import main


class TaskTest(TestCase):
    def test_display_element_from_one_to_fifteen(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(list1,main.display_element_from_one_to_fifteen())

    def test_that_function_duplicate_element_in_list(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(list1,main.duplicate_all_element_in_first_function())

    def test_remove_duplicate_of_second_function(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(list1,main.remove_duplicate_of_second_function())

    def test_add_every_third_element_in_list(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(45, main.add_every_third_element_in_list(list1))

    def test_that_function_can_add_first_middle_last_number_in_list(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(24, main.add_first_middle_last_number_in_list(list1))

    def test_that_function_can_add_first_middle_last_number_in_list_two(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16]
        self.assertEqual(25.5, main.add_first_middle_last_number_in_list(list1))

    def test_that_function_return_collection_of_numbers_without_having_duplicate(self):
        list1 = [2, 2, 5, 6, 7, 8, 9, 12, 5, 6, 8, 12, 7]
        my_set = {2, 5, 6, 7, 8, 9, 12}
        self.assertEqual(my_set,main.return_collection_of_numbers_without_having_duplicate(list1))

    def test_that_function_return_some_of_set_collection(self):
        my_set = {2, 5, 6, 7, 8, 9, 12}
        self.assertEqual(49,main.sum_collection(my_set))

    def test_that_function_return_error_message_when_collection_is_not_set(self):
        list1 = [2, 2, 5, 6, 7, 8, 9, 12, 5, 6, 8, 12, 7]
        self.assertEqual("set type required not <class 'list'>",main.sum_collection(list1))

    def test_that_function_takes_two_set_and_return_common_element_in_both(self):
        set1 = {2, 5, 6, 7, 8, 9, 15, 17}
        set2 = {3, 2, 6, 9, 10, 12, 14, 17}
        set3 = {2, 6, 9, 17}
        self.assertEqual(set3, main.find_interception(set1, set2))

    def test_that_function_return_error_message_when_either_of_the_set_is_not_type_set(self):
        list1 = [2, 5, 6, 7, 8, 9, 15, 17]
        set2 = {3, 2, 6, 9, 10, 12, 14, 17}
        result = "both collection must be set"
        self.assertEqual(result, main.find_interception(list1, set2))

    def test_function_collect_two_string_and_swap(self):
        result = "xyc abz"
        self.assertEqual(result,main.collect_two_string_and_swap_two("abc","xyz"))