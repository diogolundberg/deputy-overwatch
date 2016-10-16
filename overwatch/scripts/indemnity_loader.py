from overwatch.models import Indemnity
from overwatch.scripts import scraper
from overwatch import db
from datetime import datetime


def update_indemnities(budget_dates):
    url = "http://dadosabertos.almg.gov.br/ws/prestacao_contas/verbas_indenizatorias/legislatura_atual/deputados/{deputy_id}/{year}/{month}"
    params = []
    for budget_date in budget_dates:
        params.append({
            'deputy_id': budget_date.deputy_id,
            'year': budget_date.date.strftime('%Y'),
            'month': budget_date.date.strftime('%m'),
        })

    xml_dicts = scraper.parse_xml(url, params)

    for xml_dict in xml_dicts:
        if xml_dict['listaResumoVerba']:
            budget_summary = xml_dict['listaResumoVerba']['resumoVerba']

            if isinstance(budget_summary, dict):
                budgets = [budget_summary]
            else:
                budgets = [b for b in budget_summary]

            for budget in budgets:
                if isinstance(budget, str):
                    import pdb; pdb.set_trace()
                print(budget)
                indemnity = Indemnity()
                indemnity.deputy_id = budget['idDeputado']
                print(indemnity.deputy_id)
                indemnity.date = datetime.strptime(budget['dataReferencia']['#text'], "%Y-%m-%d")
                print(indemnity.date)
                indemnity.category_id = budget['codTipoDespesa']
                print(indemnity.category_id)
                indemnity.value = budget['valor']
                print(indemnity.value)
                indemnity.category = budget['descTipoDespesa']
                print(indemnity.category)
                db.session.merge(indemnity)
            db.session.commit()
