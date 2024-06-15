"""Gestore battaglia"""
from personaggio import Personaggio

def battaglia(pg : Personaggio, nemico: Personaggio):
    """Gestore battaglia"""
    print(f'Durante il tuo cammino incontri {nemico}')
    print('Cosa vuoi fare?')
    azioni = [(1, 'attacca')]
    print('[1] Attacca')
    for n, azione in enumerate(pg.spells, 2):
        azioni.append((n, azione))
        print(f'[{n}] {azione}')
    scelta = input()