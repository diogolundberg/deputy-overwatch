from test_base import BaseTestCase
from overwatch.scripts import deputy_loader, budget_date_loader
from overwatch.models import Deputy, BudgetDate


class DeputyLoaderTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        deputy_loader.update_deputies()
        deputies = Deputy.query.limit(5).all()
        budget_date_loader.update_budget_dates(deputies)

    @classmethod
    def tearDownClass(cls):
        Deputy.query.delete()
        BudgetDate.query.delete()

    def setUp(self):
        self.deputies = Deputy.query.all()
        self.budget_dates = BudgetDate.query.all()

    def test_every_budget_date_should_have_date_and_deputy(self):
        for budget_date in self.budget_dates:
            self.assertTrue(budget_date.date)
            self.assertTrue(budget_date.deputy_id)

    def test_every_budget_date_should_be_from_a_deputy(self):
        ids = [deputy.id for deputy in self.deputies]
        budget_dates = [d.deputy_id for d in self.budget_dates]
        self.assertTrue(set(budget_dates).issubset(ids))
