from abc import ABC, abstractmethod


class Weapon(ABC):
    def __init__(self, ammo):
        self.ammo = ammo

    @abstractmethod
    def fire(self):
        pass


class OutOfAmmoError(Exception):
    pass


class Laser(Weapon):
    def __init__(self, ammo):
        super().__init__(ammo)

    def fire(self):
        if self.ammo > 0:
            self.ammo -= 1
            print(f"Пиу-пиу! Осталось выстрелов: {self.ammo}")
        else:
            print("Батарея разряжена")


class Blaster(Weapon):
    def __init__(self, ammo):
        super().__init__(ammo)

    def fire(self):
        if self.ammo < 3:
            raise OutOfAmmoError(f"Недостаточно зарядов для выстрела из бластера. Нужно 3, осталось {self.ammo}")
        self.ammo -= 3
        print(f"Бдыщ-бдыщ! Осталось выстрелов: {self.ammo}")
