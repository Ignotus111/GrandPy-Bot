import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from api_media_wiki import ApiWiki

test = ApiWiki("Place du Général de Gaulle")

def test_pagerequest():
    assert test.pagerequest['query']['search'][0]['pageid'] == 1019357

def test_extract():
    assert test.result == """ Charles de Gaulle (/ʃaʁl də ɡol/ ), communément appelé le général de Gaulle ou parfois simplement le Général, né le 22 novembre 1890 à Lille et mort le 9 novembre 1970 à Colombey-les-Deux-Églises, es
t un militaire, résistant, homme d'État et écrivain français.
Il est notamment chef de la France libre puis dirigeant du Comité français de libération nationale pendant la Seconde Guerre mondiale, président du Gouvernement provisoire de la République française
de 1944 à 1946, président du Conseil des ministres de 1958 à 1959, instigateur de la Cinquième République, fondée en 1958, et président de la République de 1959 à 1969, étant le premier à occuper la
magistrature suprême sous ce régime.
Élevé dans une culture de grandeur nationale, Charles de Gaulle choisit une carrière d'officier. """
