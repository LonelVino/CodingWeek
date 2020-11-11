from survival import *

def test_traitement_cellule():
    assert traitement_cellule(1,1,[[0,0,0,0],[0,1,0,0],[0,0,1,1],[0,1,1,1]]) == [[0,0,0,0],[0,0,1,0],[0,0,0,1],[1,1,0,1]]
