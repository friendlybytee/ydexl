from dataclasses import dataclass


@dataclass
class Spaceship:
    name: str
    max_speed: int
    current_speed: int

    def __post_init__(self):
        if self.current_speed > self.max_speed:
            raise ValueError("Начальная скорость не может быть больше максимальной!")

    def accelerate(self, speed_increase):
        self.current_speed += speed_increase
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
            print("Осторожно! Двигатели на пределе!")

    def slow_down(self, speed_decrease):
        self.current_speed = max(0, self.current_speed - speed_decrease)
