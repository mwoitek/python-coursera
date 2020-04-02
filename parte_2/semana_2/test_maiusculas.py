from maiusculas import *

def test_maiusculas():
    assert maiusculas("Programamos em python 2?") == "P"
    assert maiusculas("Programamos em Python 3.") == "PP"
    assert maiusculas("PrOgRaMaMoS em python!") == "PORMMS"
