"""Script principale che gestisce le interazioni"""
import os
import random
import pickle
from personaggio import Personaggio
from classe import help_classes, classi
from razza import help_races, razze
from battaglia import battaglia

SALVATAGGIO = 'character.gdr'

def main() -> None:
    """Main function"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*'* 50)
    print('Benvenuto avventuriero')
    if SALVATAGGIO in os.listdir():
        with open(SALVATAGGIO, 'rb') as f:
            pg = pickle.load(f)
        print(f'È stato trovato un pg: {pg}')
    else:
        pg = crea_pg()
        with open(SALVATAGGIO, 'wb') as f:
            pickle.dump(pg, f)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Congratulazioni {pg}\nQueste sono le tue stats:')
    print(pg.get_stats())
    nemico = crea_nemico()
    battaglia(pg, nemico)

def crea_pg() -> Personaggio:
    """Inizializzazione del personaggio giocante"""
    print('Prima di iniziare la tua avventura dobbiamo definire alcune cose!\n')
    nome = input('Qual è il tuo nome: ')
    while True:
        classe_input = scelta_specifica('classe', classi, help_classes)
        razza_input = scelta_specifica('razza', razze, help_races)
        print(f'Il tuo nome è {nome}, e sei un {razza_input} {classe_input}\n')
        conferma = input('Confermi y/n: ')
        print()
        if conferma.casefold() in ['y', 'yes', 'si']:
            return Personaggio(
                nome = nome,
                classe_scelta = classe_input,
                razza_scelta = razza_input
            )

def crea_nemico() -> Personaggio:
    """Crea un npg nemico"""
    lista_nomi = [
        "Peppe Fetish", "Stella Sweppes",
        "Peppp' Le Poissoniere", "Biagio Santopaolo"
    ]
    lista_classi = [*classi.keys()]
    lista_razze = [*razze.keys()]

    return Personaggio(
        nome = random.choice(lista_nomi),
        classe_scelta = random.choice(lista_classi),
        razza_scelta = random.choice(lista_razze)
    )

def scelta_specifica(stringa, dizionario, funzione):
    """Loop per scelta classe/razza"""
    print(f'\nScegli la tua {stringa}, scrivi >help< per visualizzare le possibilità')
    while True:
        dato = input(f'Inserisci la tua {stringa}: ')
        dato = dato.casefold().strip()
        if not dato in dizionario:
            if dato == 'help':
                funzione()
            else:
                print(f'{dato} non è una {stringa} valida')
            continue
        return dato

if __name__ == '__main__':
    main()

giuseppe = 3473545403