class Diary:
    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password
        self.__islocked = True

    def unlock_diary(self, password: str):
        if self.is_not_valid(password): raise ValueError("Wrong password")
        self.__islocked = False

    def isLocked(self):
        return self.__islocked

    def is_not_valid(self, password: str):
        return self.password != password

    def lock_diary(self):
        self.__islocked = True