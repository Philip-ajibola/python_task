class Entry:
    def __init__(self, id: int, title: str, body: str):
        self.__id = id
        self.__title = title
        self.__body = body

    def get_id(self):
        return self.__id

    def update_body(self,body: str):
        self.__body = body

    def update_title(self,title: str):
        self.__body = title
