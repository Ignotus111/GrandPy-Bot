from constants import stopWords


def formulaire(contenuDuForm):
    if type(contenuDuForm) == list:
        print("C'est bon!")
    else:
        print("Pas bon! Ce n'est pas une liste!")

def motsCles(listDeMotsCles):
    if type(listDeMotsCles) == list:
        if not listDeMotsCles:
            print("Pas bon! La liste est vide")
        else:
            if any(elem in stopWords for elem in listDeMotsCles):
                print("Pas bon! Un ou plusieurs mots ne doivent pas être dans cette liste!")
            else:
                print("OK!")
    else:
        print("Pas bon! Ce n'est pas une liste!")
"""
recevoir et analyser le contenu du formulaire
    -recoit contenu form, le coupe mot par mot
    -recupère chaque mot, ne garde que les mots-clés
    -

interaction avec l'api google map
    -envoyer une requete
    -recuperer reponse
    -

interaction media wiki
    -envoyer requete
    -recuperer reponse
    -

envoyer les informations récupérée à l'utilisateur
    -donner reponse google map
    -afficher google map
    -donner reponse media wiki

envoyer du contenu html
"""
