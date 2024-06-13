"""Gestore dei PG"""
from classe import classi
from razza import razze
from dado import dado

class Personaggio:
    """Personaggio"""
    def __init__(self, nome, classe_scelta, razza_scelta) -> None:
        self.nome = nome
        self.classe = classi.get(classe_scelta)
        self.razza = razze[razza_scelta]
        self.spells = self.classe.spells
        self.livello = 1
        self.pf = 2 + self.classe._vita_iniziale
        self.pm = 2 + self.classe._magia_iniziale
        self.xp = 0
        self.forza = dado() + self.razza.forza
        self.difesa = dado() + self.razza.difesa
        self.intelligenza = dado() + self.razza.intelligenza
        self.difesa_magia = dado() + self.razza.difesa_magia

    def spell_help(self):
        """crea elenco delle spell ed illustra il funzionamento"""
        intro = f'Elenco Spell utilizzabili da {self.classe}'
        print(intro + '\n' + '-'*len(intro))
        for spell in self.classe.spells:
            print(getattr(self.classe, spell).__doc__)
        print()

    def attacca(self, target):
        """Attacca l'avversario, non consuma pm"""
        colpo, critico = self.critico()
        danni = (self.forza - target.difesa + (dado(7)-1)) * critico
        target.pf -= danni
        return f'{colpo}Infliggi {danni} a {target.nome}'

    def critico(self):
        """Definisce se il colpo è critico o no"""
        massimo = 25 - self.forza
        tiro = dado(massimo)
        if tiro == massimo:
            return ('Colpo critico, ', 2)
        elif tiro == 1:
            return ('Fallimento critico, ', 0)
        return ('', 1)

    def get_stats(self) -> str:
        """Restituisce le statistiche del personaggio"""
        *_, livello, pf, pm, xp, forza, difesa, intelligenza, difesa_magica = self.__dict__.values()
        return f'{'-'*30}\n{livello = }\n{xp = }\n{pf = }\n{pm = }\n{forza = }\n{difesa = }\n{intelligenza = }\n{difesa_magica = }\n{'-'*30}'

    def __str__(self) -> str:
        return f'{self.nome}, {self.razza} {self.classe}'

if __name__ == '__main__':
    test = Personaggio('a', 'guerriero', 'nano')
    print(*classi.values())
