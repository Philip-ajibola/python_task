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
