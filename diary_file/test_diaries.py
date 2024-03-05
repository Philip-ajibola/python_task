from unittest import TestCase

from diary_file.diaries import Diaries


class TestDiaries(TestCase):
    def setUp(self):
        self.diaries = Diaries()

    def test_that_I_can_add_diary_to_Diaries(self):
        self.diaries.add("user_name", "password")
        self.assertEqual(1, len(self.diaries.get_list_of_diary()))

    def test_that_I_can_add_more_diary_to_Diaries(self):
        self.diaries.add("user_name", "password")
        self.diaries.add("my_user_name", "password")
        self.assertEqual(2, len(self.diaries.get_list_of_diary()))

    def test_that_i_find_diary_by_user_name(self):
        self.diaries.add("user_name", "password")
        entry = self.diaries.find_by_user_name("user_name")
        self.assertEqual(entry, self.diaries.get_list_of_diary()[0])

    def test_that_if_wrong_user_name_is_entered_to_find_diary_error_is_thrown(self):
        self.diaries.add("user_name", "password")
        with self.assertRaises(ValueError):
            self.diaries.find_by_user_name("my_user")

    def test_that_I_can_delete_diary(self):
        self.diaries.add("user_name", "password")
        self.diaries.delete("user_name", "password")
        self.assertEqual(0, len(self.diaries.get_list_of_diary()))

    def test_that_diary_cant_be_deleted_if_the_password_is_wrong(self):
        self.diaries.add("user_name", "password")
        with self.assertRaises(ValueError):
            self.diaries.delete("user_name", "wrong_password")

    def test_that_diary_cant_be_deleted_if_the_username_is_wrong(self):
        diaries = Diaries()
        diaries.add("user_name", "password")
        with self.assertRaises(ValueError):
            diaries.delete("my_user_name", "password")
