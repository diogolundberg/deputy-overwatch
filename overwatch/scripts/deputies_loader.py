from overwatch.models import Deputy
from overwatch import db
import parse_data

def update_deputies():
    url = ("http://dadosabertos.almg.gov.br/ws/deputados/em_exercicio")
    xml = parse_data.get_xml_parsed_data(url)
    deputies = xml['listaDeputado']['deputado']

    for d in deputies:
        deputy = Deputy()
        deputy.name = d['nome']
        deputy.party = d['partido']
        deputy.id = d['id']
        db.session.merge(deputy)

    db.session.commit()
