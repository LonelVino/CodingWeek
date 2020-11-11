from generation import *

def test_etape_jeu_de_la_vie():
    assert etape_jeu_de_la_vie([[0,0,1],[1,1,0],[0,0,1]]) == [[0,0,1],[1,1,0],[0,0,1]]
