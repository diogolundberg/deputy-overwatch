from test_base import BaseTestCase
from overwatch.scripts import deputy_loader, budget_date_loader, indemnity_loader
from overwatch.models import Deputy, BudgetDate, Indemnity


class DeputyLoaderTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        deputy_loader.update_deputies()
        deputies = Deputy.query.limit(5).all()
        budget_date_loader.update_budget_dates(deputies)
        budget_dates = BudgetDate.query.limit(5).all()
        indemnity_loader.update_indemnities(budget_dates)

    @classmethod
    def tearDownClass(cls):
        Deputy.query.delete()
        BudgetDate.query.delete()
        Indemnity.query.delete()

    def setUp(self):
        self.deputies = Deputy.query.all()
        self.budget_dates = BudgetDate.query.all()
        self.indemnities = Indemnity.query.all()

    def test_every_indemnity_should_have_value_deputy_and_category(self):
        for indemnity in self.indemnities:
            self.assertTrue(indemnity.category)
            self.assertTrue(indemnity.value)
            self.assertTrue(indemnity.deputy_id)

    def test_every_indemnity_should_be_from_a_deputy(self):
        ids = [deputy.id for deputy in self.deputies]
        indemnities = [d.deputy_id for d in self.indemnities]
        self.assertTrue(set(indemnities).issubset(ids))
