from test_base import BaseTestCase
from factories import IndemnityFactory
from overwatch.models import Indemnity, Deputy
from sqlalchemy import desc, func
from decimal import Decimal


class IndemnityApiTests(BaseTestCase):

    def setUp(self):
        IndemnityFactory.create_batch(
            20, category='Single Category', category_id=1)

    def test_should_return_20_indemnities(self):
        response = self.client.get("/api/indemnities/")
        self.assertEqual(len(response.json['indemnities']), 20)

    def test_each_indemnity_in_json_should_have_category_and_value(self):
        response = self.client.get("/api/indemnities/")
        for indemnity in response.json['indemnities']:
            self.assertTrue(set(['category', 'value']).issubset(indemnity))

    def test_each_indemnity_in_json_should_have_a_deputy(self):
        response = self.client.get("/api/indemnities/")
        for indemnity in response.json['indemnities']:
            self.assertIn('deputy', indemnity)
            self.assertTrue(
                set(['name', 'party']).issubset(indemnity['deputy']))

    def test_should_have_one_category_with_deputies(self):
        response = self.client.get('/api/indemnities/categories/deputies/')
        categories = response.json['categories']
        self.assertEqual(len(categories), 1)
        for name, category in categories.items():
            self.assertTrue(len(category['deputies']) > 1)

    def test_deputies_grouped_by_category_should_have_total_budget(self):
        response = self.client.get('/api/indemnities/categories/deputies/')
        deputy = response.json['categories']['Single Category']['deputies'][0]
        self.assertTrue(
            set(['name', 'party', 'total_budget']).issubset(deputy.keys()))

    def test_should_have_5_deputies_per_category(self):
        response = self.client.get(
            '/api/indemnities/categories/deputies/?top=5')
        deputies = response.json['categories']['Single Category']['deputies']
        self.assertEqual(len(deputies), 5)
