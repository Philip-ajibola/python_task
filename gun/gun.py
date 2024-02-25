from gun.safety_exception import SafetyException
from gun.type import Type


class Gun:
    def __init__(self, type: Type, bullets):
        self.__type = type
        self.bullet = bullets
        self.__safety = True

    @property
    def bullet(self):
        return self.__bullet

    @bullet.setter
    def bullet(self, bullets):
        if self.__type == Type.PISTOL and (bullets < 1 or bullets > 10):
            raise ValueError("Pistol can only have between 1 to 10 bullets")
        elif self.__type == Type.SHOTGUN and (bullets < 1 or bullets > 2):
            raise ValueError("Shotgun can only have 2 bullets")
        elif self.__type == Type.RIFLE and (bullets < 1 or bullets > 25):
            raise ValueError("Rifle can only have between 1 to 25 bullets")
        elif self.__type == Type.REVOLVER and (bullets < 1 or bullets > 150):
            raise ValueError("Revolver can only have between 1 to 150 bullets")
        self.__bullet = bullets

    def number_of_bullets(self):
        return self.__bullet

    def shoot(self):
        if self.__bullet <= 0:
            raise ValueError("Bullet is finished")
        elif self.__safety:
            raise SafetyException()
        self.__bullet -= 1

    def reload(self):
        if self.__type == Type.PISTOL:
            self.__bullet = 10
        elif self.__type == Type.SHOTGUN:
            self.__bullet = 2
        elif self.__type == Type.RIFLE:
            self.__bullet = 25
        elif self.__type == Type.REVOLVER:
            self.__bullet = 150

    def safety_check(self):
        return self.__safety

    def toggle_safety(self):
        self.__safety = not self.__safety
