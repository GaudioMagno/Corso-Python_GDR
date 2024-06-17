import pickle
import random

class Dado:
    def __init__(self, facce) -> None:
        self.facce = facce

    def tira(self):
        return random.randint(1,self.facce)

    def __repr__(self) -> str:
        return f'Dado a {self.facce} facce'

dadi = {
    "d6" : Dado(6),
    "d10" : Dado(10),
    "d20" : Dado(20),
}

with open('dadi', 'wb') as f:
    pickle.dump(dadi, f)
