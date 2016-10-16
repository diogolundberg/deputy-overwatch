from test_base import BaseTestCase
from factories import DeputyFactory


class DeputyApiTests(BaseTestCase):

    def setUp(self):
        DeputyFactory.create_batch(10)

    def test_should_return_10_deputies(self):
        response = self.client.get("/api/deputies/")
        self.assertEqual(len(response.json['deputies']), 10)

    def test_each_deputy_in_json_should_have_name_and_party(self):
        response = self.client.get("/api/deputies/")
        for deputy in response.json['deputies']:
            self.assertTrue(set(['name', 'party']).issubset(deputy))
