from overwatch.models import Deputy
from overwatch.scripts import scraper
from overwatch import db


def update_deputies():
    url = "http://dadosabertos.almg.gov.br/ws/deputados/em_exercicio"
    xml_dict = scraper.parse_xml(url)[0]

    deputies = xml_dict['listaDeputado']['deputado']
    for d in deputies:
        deputy = Deputy()
        deputy.name = d['nome']
        deputy.party = d['partido']
        deputy.id = d['id']
        db.session.merge(deputy)

    db.session.commit()
