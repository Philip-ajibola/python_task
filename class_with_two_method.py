class Methods:
    def __init__(self):
        self.string = ""

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self,string):
        self._string = string


