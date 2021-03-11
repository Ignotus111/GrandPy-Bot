import requests
from app.apis.parsefunc import parser


class ApiWiki():
    def __init__(self, searchpage):
        self.searchpage = searchpage.lower()
        self.cleansearch = parser(self.searchpage)
        self.session = requests.Session()
        self.url = "https://fr.wikipedia.org/w/api.php"
        self.pageparams = {
            "action": "query",
            "list": "search",
            "srsearch": self.cleansearch,
            "format": "json"
        }
        """
        Searching all results from user request.
        """
        self.pagerequest = (self.session.get(url=self.url, params=self.pageparams)).json()
        """
        Takes the first result, get its page id (pageids) and then makes a
        request of the page.
        """
        self.searchparams = {
            "action": "query",
            "prop": "extracts",
            "exsentences": "3",
            "pageids": self.pagerequest['query']['search'][0]['pageid'],
            "explaintext": "1",
            "formatversion": "2",
            "format": "json"
        }
        self.searchrequest = (self.session.get(url=self.url, params=self.searchparams)).json()
        self.result = self.result()

    def result(self):
        """
        Takes the 'extract' of the page. If the page does not exist, return an
        error.
        """
        try:
            return self.searchrequest['query']['pages'][0]['extract']
        except KeyError:
            return "Ma mémoire me joue des tours! Je n'ai rien à te raconter sur ce lieu."
