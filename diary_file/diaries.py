from diary_file.diary import Diary


class Diaries:
    def __init__(self):
        self.__diaries = []

    def get_list_of_diary(self):
        return self.__diaries

    def add(self, user_name: str, password: str):
        diary = Diary(user_name, password)
        self.__diaries.append(diary)

    def find_by_user_name(self, user_name: str):
        for diary in self.__diaries:
            if diary.get_user_name() == user_name:
                return diary
            else:
                raise ValueError("Diary Not Found")

    def delete(self, user_name: str, password: str):
        diary = self.find_by_user_name(user_name)
        if diary.is_not_valid(password): raise ValueError("Wrong Password")
        self.__diaries.remove(diary)
