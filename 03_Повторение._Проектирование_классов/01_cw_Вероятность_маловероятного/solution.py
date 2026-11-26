class ImprobabilityDrive:
    def __init__(self, probability):
        self.probability = probability

    def get_probability(self):
        return self.probability

    def set_probability(self, value):
        if not 0 <= value <= 1:
            raise ValueError("Вероятность может быть только в диапазоне [0, 1]")
        self.probability = value

    def jump(self):
        if self.probability < 0.5:
            return "Прыжок через гиперпространство совершён!"
        return "Ничего не произошло, всё слишком предсказуемо"
