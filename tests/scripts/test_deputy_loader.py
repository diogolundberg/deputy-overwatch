from test_base import BaseTestCase
from overwatch.scripts import deputy_loader
from overwatch.models import Deputy


class DeputyLoaderTests(BaseTestCase):


    def setUp(self):
        deputy_loader.update_deputies()
        self.deputies = Deputy.query.all()


    def test_should_load_77_deputies(self):
        self.assertEqual(len(self.deputies), 77)


    def test_every_deputy_should_have_name(self):
        deputy = self.deputies[0]
        self.assertTrue(deputy.name)


    def test_every_deputy_should_have_id(self):
        deputy = self.deputies[0]
        self.assertTrue(deputy.id)


    def test_every_deputy_should_have_party(self):
        deputy = self.deputies[0]
        self.assertTrue(deputy.party)


    def test_should_overwrite_existing_data(self):
        deputy_loader.update_deputies()
        self.assertEqual(len(Deputy.query.all()), 77)
