from dataclasses import dataclass
from functools import total_ordering

G = 6.67430e-11


@total_ordering
@dataclass
class Planet:
    name: str
    radius: float
    gravity: float = 9.8

    def weight_on_planet(self, m, r):
        return self.gravity * self.radius ** 2 * m / (self.radius + r) ** 2

    def planet_mass(self):
        return self.gravity * self.radius ** 2 / G

    def __lt__(self, other):
        return (self.radius, self.gravity, self.name) < (other.radius, other.gravity, other.name)
