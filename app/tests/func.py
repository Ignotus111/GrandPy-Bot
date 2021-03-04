import requests

def wiki_api(SEARCHPAGE):
    S = requests.Session()

    URL = "https://fr.wikipedia.org/w/api.php"


    PARAMS = {
        "action": "query",
        "prop": "extracts",
        "exsentences": "3",
        "titles": SEARCHPAGE,
        "explaintext": "1",
        "formatversion":"2",
        "format":"json"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    result = DATA
    try:
        result['query']['pages'][0]['extract']
    except KeyError:
        return "Ma mémoire me joue des tours! Je n'ai rien à te raconter sur ce lieu."
