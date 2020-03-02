from menor_nome import *

def test_menor_nome():
    assert menor_nome(["maria", "josé", "PAULO", "Catarina"]) == "José"
    assert menor_nome(["maria", " josé  ", "  PAULO", "Catarina  "]) == "José"
    assert menor_nome(["Bárbara", "JOSÉ  ", "Bill"]) == "José"
