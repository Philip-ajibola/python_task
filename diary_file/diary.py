from typing import List, Any

from diary_file.entry import Entry


class Diary:
    def __init__(self, user_name: str, password: str):
        self.__entries = []
        self.__user_name = user_name
        self.__password = password
        self.__isLocked = True
        self.__entry_id_generator = 0

    def unlock_diary(self, password: str):
        if self.is_not_valid(password): raise ValueError("Wrong password")
        self.__isLocked = False

    def isLocked(self) -> bool:
        return self.__isLocked

    def is_not_valid(self, password: str) -> bool:
        return self.__password != password

    def lock_diary(self):
        self.__isLocked = True

    def create_entry(self, title: str, body: str):
        entry_id = self.__generate_entry_id()
        entry = Entry(entry_id, title, body)
        self.__entries.append(entry)

    def __generate_entry_id(self) -> int:
        self.__entry_id_generator += 1
        return self.__entry_id_generator

    def get_element_in_entry(self) -> list[Any]:
        return self.__entries

    def deleteEntry(self, entry_id: int):
        entry = self.find_entry(entry_id)
        self.__entries.remove(entry)

    def find_entry(self, entry_id: int) -> Entry:
        for entry in self.__entries:
            print(entry.get_id())
            if entry.get_id() == entry_id:
                return entry
            else:
                raise ValueError("Entry Does Not Exist ")

    def update_entry(self, entry_id: int,updated_title,updated_body):
        entry_to_update = self.find_entry(entry_id)
        for entry in self.__entries:
            if entry == entry_to_update:
                entry.update_title(updated_title)
                entry.update_body(updated_body)

    def get_user_name(self):
        return self.__user_name

    def getEntryNumber(self,title):
        for entry in self.__entries:
            if entry.get_title() == title:
                return entry.get_id()




