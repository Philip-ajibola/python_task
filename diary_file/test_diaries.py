from unittest import TestCase

from diary_file.diaries import Diaries


class TestDiaries(TestCase):
    def test_that_I_can_add_to_Diaries(self):
        diaries = Diaries()
        diaries.add("user_name", "password")
        self.assertEqual(1, len(diaries.get_list_of_diary()))

    def test_that_i_find_diary_by_user_name(self):
        diaries = Diaries()
        diaries.add("user_name", "password")
        entry = diaries.find_by_user_name("user_name")
        self.assertEqual(entry, diaries.get_list_of_diary()[0])

    def test_that_I_can_delete_diary(self):
        diaries = Diaries()
        diaries.add("user_name", "password")
        diaries.delete("user_name","password")
        self.assertEqual(0, len(diaries.get_list_of_diary()))