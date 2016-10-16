from test_base import BaseTestCase
from overwatch.scripts import deputy_loader, budget_date_loader, indemnity_loader
from overwatch.models import Deputy, BudgetDate, Indemnity


class ScraperTests(BaseTestCase):

    def setUp(self):
        deputy_loader.update_deputies()
        self.deputies = Deputy.query.all()
        budget_date_loader.update_budget_dates(self.deputies)
        self.budget_dates = BudgetDate.query.all()
        indemnity_loader.update_indemnities(self.budget_dates)
        self.indemnities = Indemnity.query.all()

    def test_should_load_77_deputies(self):
        self.assertEqual(len(self.deputies), 77)

    def test_should_load_1448_buget_dates(self):
        self.assertEqual(len(self.budget_dates), 1448)

    def test_should_load_7052_indemnities(self):
        self.assertEqual(len(self.indemnities), 7052)
