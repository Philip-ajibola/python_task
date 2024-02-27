from unittest import TestCase
from diary_file.diary import Diary


class TestDiary(TestCase):
    def test_that_diary_is_unlock_at_point_of_creation(self):
        diary = Diary("userName", "password")
        self.assertTrue(diary.isLocked())

    def test_that_I_can_unlock_diary(self):
        diary = Diary("userName", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.isLocked())

    def test_that_i_can_lock_diary(self):
        diary = Diary("userName", "password")
        diary.unlock_diary("password")
        diary.lock_diary()
        self.assertTrue(diary.isLocked())

    def test_that_entry_can_be_created(self):
        diary = Diary("user_name", "password")
        diary.create_entry("body", "title")
        self.assertEqual(1, len(diary.get_element_in_entry()))

    def test_that_i_can_find_entry_by_id(self):
        diary = Diary("user_name", "password")
        diary.create_entry("body", "title")
        expected = diary.find_entry(1)
        print(expected)
        self.assertEqual(expected, diary.get_element_in_entry()[0])

    def test_that_i_can_delete_entry(self):
        diary = Diary("user_name", "password")
        diary.create_entry("body", "title")
        self.assertEqual(1, len(diary.get_element_in_entry()))
        diary.deleteEntry(1)
        self.assertEqual(0, len(diary.get_element_in_entry()))

