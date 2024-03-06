from unittest import TestCase
from diary_file.diary import Diary


class TestDiary(TestCase):
    def test_that_diary_is_lock_at_point_of_creation(self):
        diary = Diary("userName", "password")
        self.assertTrue(diary.isLocked())

    def test_that_I_can_unlock_diary(self):
        diary = Diary("userName", "password")
        diary.unlock_diary("password")
        self.assertFalse(diary.isLocked())

    def test_that_diary_cant_unlock_with_wrong_password(self):
        diary = Diary("userName", "password")
        with self.assertRaises(ValueError):
            diary.unlock_diary("wrong_password")
        self.assertTrue(diary.isLocked())

    def test_that_i_can_lock_diary(self):
        diary = Diary("userName", "password")
        diary.unlock_diary("password")
        diary.lock_diary()
        self.assertTrue(diary.isLocked())

    def test_that_entry_can_be_created(self):
        diary = Diary("user_name", "password")
        diary.create_entry("title", "body")
        self.assertEqual(1, len(diary.get_element_in_entry()))

    def test_that_i_can_find_entry_by_id(self):
        diary = Diary("user_name", "password")
        diary.create_entry("title", "body")
        expected = diary.find_entry(1)
        print(expected)
        self.assertEqual(expected, diary.get_element_in_entry()[0])

    def test_that_i_can_delete_entry_with_entryId(self):
        diary = Diary("user_name", "password")
        diary.create_entry("title", "body")
        self.assertEqual(1, len(diary.get_element_in_entry()))
        diary.delete_entry(1)
        self.assertEqual(0, len(diary.get_element_in_entry()))

    def test_that_i_cant_delete_entry_if_entryId_is_wrong(self):
        diary = Diary("user_name", "password")
        diary.create_entry("title", "body")
        self.assertEqual(1, len(diary.get_element_in_entry()))
        with self.assertRaises(ValueError):
            diary.delete_entry(2)
        self.assertEqual(1, len(diary.get_element_in_entry()))

    def test_that_i_can_update_entry(self):
        diary = Diary("user_name", "password")
        diary.create_entry("title", "body")
        entry = diary.find_entry(1)
        diary.update_entry(1, "updated_title", "updated_body")
        self.assertEqual(entry.get_title(), "updated_title")

    def test_that_i_cant_update_entry_when_entryId_is_wrong(self):
        diary = Diary("user_name", "password")
        diary.create_entry("title", "body")
        with self.assertRaises(ValueError):
            diary.update_entry(2, "updated_title", "updated_body")
