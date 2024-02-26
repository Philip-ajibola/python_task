from diary_file.entry import Entry


class Diary:
    def __init__(self, user_name: str, password: str):
        self.__entries = []
        self.user_name = user_name
        self.password = password
        self.__islocked = True
        self.__entry_id_generator = 0

    def unlock_diary(self, password: str):
        if self.is_not_valid(password): raise ValueError("Wrong password")
        self.__islocked = False

    def isLocked(self) -> bool:
        return self.__islocked

    def is_not_valid(self, password: str) -> bool:
        return self.password != password

    def lock_diary(self):
        self.__islocked = True

    def create_entry(self, title: str, body: str):
        entry_id = self.__generate_entry_id()
        entry = Entry(entry_id, title, body)
        self.__entries.append(entry)

    def __generate_entry_id(self) -> int:
        self.__entry_id_generator += 1
        return self.__entry_id_generator

    def get_number_of_entry(self) -> int:
        return len(self.__entries)

    def deleteEntry(self, entry_id: int):
        self.find_entry(entry_id)

    def find_entry(self, entry_id: int) -> Entry:
        for entry in self.__entries:
            if entry.getId() == id:
                return entry
