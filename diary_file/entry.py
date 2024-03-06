class Entry:
    def __init__(self, id: int, title: str, body: str):
        self.__id = id
        self.__title = title
        self.__body = body

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def update_body(self, body: str):
        self.__body = body

    def update_title(self, title: str):
        self.__title = title

    def __repr__(self):
        return (f"Title: {self.__title} \n\n\nBody{self.__body}")
