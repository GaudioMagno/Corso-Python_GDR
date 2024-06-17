import pickle
import random
class Dado:
    def __init__(self, facce) -> None:
        self.facce = facce

    def tira(self):
        return random.randint(1,self.facce)

    def __repr__(self) -> str:
        return f'Dado a {self.facce} facce'

with open('dadi', 'rb') as f:
    dadi = pickle.load(f)

print(dadi)