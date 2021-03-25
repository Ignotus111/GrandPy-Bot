
from app.apis.parsefunc import parser

def test_lower_parser():
    assert parser("OpenClassrooms") == "openclassrooms"

def test_special_char():
    assert parser("';:!?,") == ""

def test_remove_stopwords():
    assert parser("Bonjour ! Quelle est l'adresse d'Openclassrooms ?") == "openclassrooms"
