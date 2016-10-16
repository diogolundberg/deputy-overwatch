from test_base import BaseTestCase
from nose.plugins.attrib import attr
from overwatch.scripts import deputy_loader, budget_date_loader
from overwatch.models import Deputy, BudgetDate

class BudgetDateLoaderTests(BaseTestCase):

    def setUp(self):
        deputy_loader.update_deputies()
        self.deputies = Deputy.query.all()
        budget_date_loader.update_budget_dates(self.deputies)
        self.buget_dates = BudgetDate.query.all()

    def test_should_load_1448_buget_dates(self):
        self.assertEqual(len(self.buget_dates), 1448)

    def test_should_overwrite_existing_data(self):
        budget_date_loader.update_budget_dates(self.deputies)
        self.assertEqual(len(BudgetDate.query.all()), 1448)
