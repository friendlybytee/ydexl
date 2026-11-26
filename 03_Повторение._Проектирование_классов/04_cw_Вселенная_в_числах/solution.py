class VogonNumber:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return VogonNumber(self.n + other)

    def __sub__(self, other):
        return VogonNumber(self.n - other)

    def __mul__(self, other):
        return VogonNumber(self.n * other)

    def __truediv__(self, other):
        return VogonNumber(round(self.n / other))

    def __iadd__(self, other):
        self.n += other
        return self

    def __floordiv__(self, other):
        if self.n / other < 42:
            raise ZeroDivisionError("Это худшее стихотворение в моей жизни!")
        return VogonNumber(self.n // other)

    def __str__(self):
        return f"Число Вселенной: {self.n}"
