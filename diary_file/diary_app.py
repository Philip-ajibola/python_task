import time

from diary_file.diary import Diary
from tkinter import simpledialog, messagebox


class DiaryApp:

    @staticmethod
    def create_dairy():

        user_name = DiaryApp._input_("Welcome to My Diary \n\nThe best diary you can ever think of enjoy the App\n\n "
                                     "Enter Your User_name ")
        if len(user_name) == 0 or user_name.isdigit():
            DiaryApp.output("name can't be empty or Digit ")
            DiaryApp.create_dairy()
        password = DiaryApp._input_("set password ")
        if len(password) == 0:
            DiaryApp.output("password need to need be set")
            DiaryApp.create_dairy()
        DiaryApp.__verify_password(password)
        diary = Diary(user_name, password)
        time.sleep(0.5)
        DiaryApp.output("Diary Created Successfully")
        DiaryApp.display(diary)

    @staticmethod
    def lock_diary(diary: Diary):
        if diary.isLocked():
            DiaryApp.output("Diary is already locked")
        else:
            diary.lock_diary()
            time.sleep(0.5)
            DiaryApp.output("Diary Successfully Locked")
        DiaryApp.display(diary)

    @staticmethod
    def unLock_diary(diary: Diary):
        if diary.isLocked():
            try:
                password = DiaryApp._input_("Enter Password To Unlock Diary")
                diary.is_not_valid(password)
                time.sleep(0.5)
                DiaryApp.output("Diary UnLocked")
            except Exception as e:
                DiaryApp.output(f"{e}")
            finally:
                DiaryApp.display(diary)
        else:
            DiaryApp.output("Diary is Unlocked Already")

    @staticmethod
    def find_entry_by_id(diary: Diary):
        try:
            DiaryApp.__check_if_diary_unlock(diary)
            user_response = int(DiaryApp._input_("Enter your EntryId"))
            returned_entry = diary.find_entry(user_response)
            DiaryApp.output(f"{returned_entry}")

        except Exception as e:
            DiaryApp.output(f"{e}")
        finally:
            DiaryApp.display(diary)

    @staticmethod
    def add_entry(diary: Diary):
        try:
            DiaryApp.__check_if_diary_unlock(diary)
            title = DiaryApp._input_("Enter Title of Entry")
            body = DiaryApp._input_("Enter body Of The Entry")
            diary.create_entry(title, body)
            time.sleep(0.5)
            DiaryApp.output("Entry Successfully Added")
            DiaryApp.output(f"Your EntryId is {diary.getEntryNumber(title)} \nMake sure you don't forget your entry id")
        except Exception as e:
            DiaryApp.output(f"{e}")
        finally:
            DiaryApp.display(diary)

    @staticmethod
    def output(message: str):
        messagebox.showinfo("Output", message)

    @staticmethod
    def _input_(message: str):
        return simpledialog.askstring("Input", message)

    @staticmethod
    def update_entry(diary: Diary):
        try:
            DiaryApp.__check_if_diary_unlock(diary)
            entry_id = int(DiaryApp._input_("Enter entryId"))
            new_title = DiaryApp._input_("Enter Title")
            new_body = DiaryApp._input_("Enter Body")
            diary.update_entry(entry_id, new_title, new_body)
            time.sleep(0.5)
            DiaryApp.output("Entry Updated Successfully ")
        except Exception as e:
            DiaryApp.output(f"{e}")
        finally:
            DiaryApp.display(diary)

    @staticmethod
    def delete_entry(diary: Diary):
        try:
            DiaryApp.__check_if_diary_unlock(diary)
            entry_id = int(DiaryApp._input_("Enter entryId"))
            diary.delete_entry(entry_id)
            time.sleep(0.5)
            DiaryApp.output("Entry Deleted")
        except Exception as e:
            DiaryApp.output(f"{e}")
        finally:
            DiaryApp.display(diary)

    @staticmethod
    def __verify_password(password: str):
        password2 = DiaryApp._input_("Verify Password")
        if password2 == password:
            return password
        else:
            raise ValueError("Wrong Input")

    @staticmethod
    def __check_if_diary_unlock(diary: Diary):
        if diary.isLocked():
            password = DiaryApp._input_("Entry is Locked \nEnter Password Lock Entry")
            diary.is_not_valid(password)
            diary.unlock_diary(password)
            return True
        return False

    @staticmethod
    def display(diary):
        user_input = DiaryApp._input_("""
                    <<<<<<< What would you love to do today >>>>>
                    
                        [(1)] Add Entry         [(2)] Update Entry
                        
                        [(3)] Find Entry        [(4)] Delete Entry
                        
                        [(5)] Lock Entry        [(6)] Exit App
                    """)
        if len(user_input) == 0:
            DiaryApp.output("Please Choose an option 1-6 ")
            DiaryApp.display(diary)

        DiaryApp.display_response_to_user_input(diary, int(user_input))

    @staticmethod
    def display_response_to_user_input(diary, user_input):
        match user_input:
            case 1:
                DiaryApp.add_entry(diary)
            case 2:
                DiaryApp.update_entry(diary)
            case 3:
                DiaryApp.find_entry_by_id(diary)
            case 4:
                DiaryApp.delete_entry(diary)
            case 5:
                DiaryApp.lock_diary(diary)
            case 6:
                DiaryApp.output("Bye!!")
            case _:
                DiaryApp.output("Wrong Input Please Pay Attention ")
                DiaryApp.display(diary)

    @staticmethod
    def main_menu():
        DiaryApp.create_dairy()


if __name__ == '__main__':
    DiaryApp.main_menu()
