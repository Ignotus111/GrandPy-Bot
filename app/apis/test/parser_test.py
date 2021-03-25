import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from parsefunc import parser

def test_lower_parser():
    assert parser("OpenClassrooms") == "openclassrooms"

def test_special_char():
    assert parser("';:!?,") == ""

def test_remove_stopwords():
    assert parser("Bonjour ! Quelle est l'adresse d'Openclassrooms ?") == "openclassrooms"
