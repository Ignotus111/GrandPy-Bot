from app.apis.parsefunc import parser


def test_parser():
    assert parser("OpenClassrooms") == "openclassrooms"

    assert parser("';:!?,") == ""

    assert (
        parser("Bonjour ! Quelle est l'adresse d'Openclassrooms ?") == "openclassrooms"
    )
