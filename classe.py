"""Gestore delle classi"""
from abc import ABC
from dado import dado

classi = {}

class Classe(ABC):
    """Classe astratta base"""
    def __init__(self, vita_iniziale, magia_iniziale) -> None:
        self._vita_iniziale = vita_iniziale
        self._magia_iniziale = magia_iniziale

    def __repr__(self) -> str:
        return self.__class__.__name__

class Guerriero(Classe):
    """Guerriero:

modificatori:
    • forza + 2
    • intelligenza - 1
    • difesa magica - 1

abilità iniziale:
    Doppio attacco -> Attacca 2 volte contemporaneamente | 2 pm
    """
    def __init__(self) -> None:
        super().__init__(vita_iniziale = 10, magia_iniziale = 4)
        self.spells = [x for x in self.__dir__() if not x.startswith('_')]

    def doppio_attacco(self):
        """Doppio attacco -> Attacca 2 volte contemporaneamente | 2 pm"""

classi['guerriero'] = Guerriero()

class Mago(Classe):
    """Mago:

modificatori
    • intelligenza + 2
    • forza - 2

abilità iniziale:
    Palla di fuoco -> Lancia una potente palla di fuoco sul nemico, danni 2d6 | 3 pm
    """
    def __init__(self) -> None:
        super().__init__(vita_iniziale = 6, magia_iniziale = 10)
        self.spells = [x for x in self.__dir__() if not x.startswith('_')]

    def palla_di_fuoco(self):
        """Palla di fuoco -> Lancia una potente palla di fuoco sul nemico, danni 2d6 | 3 pm"""

classi['mago'] = Mago()

class Druido(Classe):
    """Druido:

modificatori
    • forza + 1
    • intelligenza + 1
    • difesa - 1
    • difesa magica - 1

abilità iniziale:
    Dono della natura -> Cura di 2d4 | 3 pm
    """
    def __init__(self) -> None:
        super().__init__(vita_iniziale = 8, magia_iniziale = 6)
        self.spells = [x for x in self.__dir__() if not x.startswith('_')]

    def dono_della_natura(self, target):
        """Dono della natura -> Cura di 2d4 | 3 pm"""
        target.pf += dado(4, 2)
        target.pm -= 3

classi['druido'] = Druido()

class Hunter(Classe):
    """
Hunter

modificatori
    • forza + 1
    • intelligenza 0
    • difesa 0
    • difesa magica + 1

abilità iniziale:
    Trappola mortale -> Piazza una trappola che infligge 2d6 | 4 pm
    """
    def __init__(self) -> None:
        super().__init__(vita_iniziale = 14, magia_iniziale = 8)
        self.spells = [x for x in self.__dir__() if not x.startswith('_')]

    def trappola_mortale(self, target):
        """Trappola mortale -> Piazza una trappola che infligge 2d6 | 4 pm"""

classi['hunter'] = Hunter()

def help_classes() -> None:
    """Genera una descrizione delle classi"""
    print('-'*50)
    print('Descrizione Classi')
    for a in classi.values():
        print('-'*50)
        print(a.__doc__)
    print('-'*50)
