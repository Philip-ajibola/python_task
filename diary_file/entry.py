class Entry:
    def __init__(self, id: int, title: str, body: str):
        self.__id = id
        self.__title = title
        self.__body = body

    def get_id(self):
        return self.__id
