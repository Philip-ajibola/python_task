class SafetyException(Exception):
    def __init__(self):
        super().__init__("Gun can't be use while safety is on")