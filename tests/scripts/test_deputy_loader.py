from test_base import BaseTestCase
from overwatch.scripts import deputy_loader
from overwatch.models import Deputy


class DeputyLoaderTests(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        deputy_loader.update_deputies()

    @classmethod
    def tearDownClass(cls):
        Deputy.query.delete()

    def setUp(self):
        self.deputies = Deputy.query.all()

    def test_should_load_77_deputies(self):
        self.assertEqual(len(self.deputies), 77)

    def test_every_deputy_should_have_name_id_and_party(self):
        for deputy in self.deputies:
            self.assertTrue(deputy.name)
            self.assertTrue(deputy.id)
            self.assertTrue(deputy.party)

    def test_should_overwrite_existing_data(self):
        deputy_loader.update_deputies()
        self.assertEqual(len(self.deputies), 77)
