class Human:
    number_of_eyes = 2

    def __init__(self, height: float, gender: str, name: str):
        self.height = height
        self.gender = gender
        self.name = name

    def sleep(self):
        print(f"{self.name} is sleeping..... ")

    def eating(self):
        print(f"{self.name} is eating...... ")

    def __str__(self):
        return f"{self.name} {self.height} {self.gender}"


bolaji = Human(4.1, 'male',"bolaji")
hannah = Human(3.5, 'female',"hannah")

bolaji.sleep()
print(bolaji)
