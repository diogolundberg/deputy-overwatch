from overwatch.models import BudgetDate
from overwatch.scripts import scraper
from overwatch import db
from datetime import datetime


def update_budget_dates(deputies):
    url = "http://dadosabertos.almg.gov.br/ws/prestacao_contas/verbas_indenizatorias/" + \
        "legislatura_atual/deputados/{id}/datas"
    params = [{'id': deputy.id} for deputy in deputies]
    xml_dicts = scraper.parse_xml(url, params)

    for xml_dict in xml_dicts:
        final_budget = xml_dict['listaFechamentoVerba']['fechamentoVerba']

        if isinstance(final_budget, dict):
            final_budget = [final_budget]
        else:
            budgets = [b for b in final_budget]

        for budget in budgets:
            budget_date = BudgetDate()
            budget_date.deputy_id = budget['idDeputado']
            budget_date.date = datetime.strptime(
                budget['dataReferencia']['#text'], "%Y-%m-%d")
            db.session.merge(budget_date)
        db.session.commit()
