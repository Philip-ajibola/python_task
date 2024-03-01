import time

from diary_file.diary import Diary
from tkinter import simpledialog, messagebox


class DiaryApp:

    @staticmethod
    def create_dairy():
        user_name = DiaryApp._input_("Enter Your User_name ")
        password = DiaryApp.verify_password(DiaryApp._input_("set password "))
        diary = Diary(user_name, password)

    @staticmethod
    def lock_diary(diary: Diary):
        diary.lock_diary()
        time.sleep(0.5)
        DiaryApp.output("Diary Successfully Locked")

    @staticmethod
    def unLock_diary(diary: Diary):
        if diary.isLocked():
            try:
                password = DiaryApp._input_("Enter Password To Unlock Diary")
                diary.is_not_valid(password)
            except Exception as e:
                DiaryApp.output(f"{e}")

    @staticmethod
    def find_entry_by_id(diary: Diary):
        try:
            user_response = int(DiaryApp._input_("Enter your EntryId"))
            returned_entry = diary.find_entry(user_response)
            DiaryApp.output(f"{returned_entry}")

        except Exception as e:
            DiaryApp.output(f"{e}")

    @staticmethod
    def output(message: str):
        messagebox.showinfo("Output", message)

    @staticmethod
    def _input_(message: str):
        return simpledialog.askstring("Input", message)

    @staticmethod
    def verify_password(password: str):
        password2 = DiaryApp._input_("Verify Password")
        if password2 == password:
            return password
        else:
            raise ValueError("Wrong Input")
