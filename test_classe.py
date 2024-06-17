import random

class Quadrato:
    def __init__(self, lato) -> None:
        self.lato = lato

    @property
    def area(self):
        return self.lato**2

d = Quadrato(5)
print(d.area)
d.lato = 10
print(d.lato)
print(d.area)
