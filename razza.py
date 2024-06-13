"""Gestore delle razze"""
from abc import ABC

razze = {}

class Razze(ABC):
    """Razza astratta base"""
    def __init__(self, forza, difesa, intelligenza, difesa_magia) -> None:
        self.forza = forza
        self.difesa = difesa
        self.intelligenza = intelligenza
        self.difesa_magia = difesa_magia

    def __repr__(self) -> str:
        return self.__class__.__name__

class Umano(Razze):
    """Umano:

modificatori:
    • intelligenza + 1
    • difesa magica + 1

abilità raziale:
    Magia amplificata -> La tua prossima magia ha il 90% di possibilità di arrecare un critico
    """
    def __init__(self) -> None:
        super().__init__(0, 0, 1, 1)

razze['umano'] = Umano()

class Nano(Razze):
    """Nano:

modificatori:
    • forza + 2
    • difesa + 1
    • intelligenza - 1

abilità raziale:
    Impeto Nanico -> Sferra un attacco che ha il 90% di possibilità di arrecare un critico
    """
    def __init__(self) -> None:
        super().__init__(2, 1, -1, 1)

razze['nano'] = Nano()

class Elfo(Razze):
    """Elfo:

modificatori:
    • forza + 1
    • intelligenza + 1
    • difesa magica + 1

abilità raziale:
    Destrezza Elfica -> Usa la somma tra l'intelligenza e la forza per sferrare l'attacco senza modificatore
    """
    def __init__(self) -> None:
        super().__init__(1, 0, 1, -1)

razze['elfo'] = Elfo()

class Halfling(Razze):
    """Halfling:

modificatori:
    • intelligenza + 2
    • difesa magica + 1

abilità raziale:
    Seconda colazione -> Recupera 1d6 pf
    """
    def __init__(self) -> None:
        super().__init__(0, 0, 2, 1)

    def seconda_colazione(self, target):
        """Seconda colazione -> Recupera 1d6 pf"""

razze['halfling'] = Halfling()

def help_races() -> None:
    """Genera una descrizione delle classi"""
    print('-'*50)
    print('Descrizione Razze')
    for a in razze.values():
        print('-'*50)
        print(a.__doc__)
    print('-'*50)
