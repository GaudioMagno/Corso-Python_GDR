"""Tira 1 dado da x facce n volte con la funziona dado"""
from random import randint

def dado(facce : int = 6, volte : int = 1) -> int:
    """
    Tira 1 dado da x facce n volte

    + Default facce -> 6
    + Default volte -> 1
    """
    return sum(randint(1, facce) for _ in range(volte))
