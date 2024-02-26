from unittest import TestCase
from diary_file.diary import Diary


class TestDiary(TestCase):
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
        diary = Diary("user_name","password")
        diary.create_entry("body","title")
        self.assertEqual(1,diary.get_number_of_entry())

    def test_that_i_can_delete_entry(self):
        diary = Diary("user_name","password")
        diary.create_entry("body","title")
        self.assertEqual(1,diary.get_number_of_entry())
        diary.deleteEntry(1)
        self.assertEqual(0, diary.get_number_of_entry())

