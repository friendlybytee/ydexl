class Traveler:
    def __init__(self, name, towel=True):
        self.name = name
        self.towel = towel

    def needs_ride(self):
        return f"{self.name} голосует на дороге..."


class Arthur(Traveler):
    def __init__(self):
        super().__init__("Артур", True)

    def needs_ride(self):
        return super().needs_ride()[:-3] + ", в панике размахивая полотенцем."


class Alien(Traveler):
    def __init__(self, name, towel=True, species=""):
        super().__init__(name, towel)
        self.species = species
        if species == "Вогон":
            self.towel = False

    def needs_ride(self):
        return super().needs_ride()[:-3] + f": {self.species} издаёт непонятные звуки, требуя подвезти."
