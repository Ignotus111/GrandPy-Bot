from app.apis.constants import STOPWORDS
#from constants import STOPWORDS


def parser(textToParse):
    """
    Takes class argument (the place user is searching),
    replaces special character by a space then split every word in a list.
    Look if a word is in stopwords if it is, deletes it.
    And eventually join all the left words in one string.
    """
    clean = []
    cleantext = textToParse.lower().replace(",", " ").replace("!", " ").replace(".", " ").replace("?", " ").replace(";", " ").replace("'", " ").replace(":"," ")
    splitedText = cleantext.split()
    for elem in splitedText:
        if elem not in STOPWORDS:
            clean.append(elem)
        else:
            pass
    separator = " "
    clean = separator.join(clean)
    return clean
