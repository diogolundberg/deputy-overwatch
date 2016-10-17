from test_base import BaseTestCase
from factories import IndemnityFactory
from overwatch.models import Indemnity


class IndemnityApiTests(BaseTestCase):


    def setUp(self):
        IndemnityFactory.create_batch(
            20, category='Single Category', category_id=1)

    def tearDown(self):
        Indemnity.query.delete()

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

    def test_indemnities_grouped_by_category_should_have_one_category(self):
        response = self.client.get("/api/indemnities/categories/")
        self.assertIn('categories', response.json)
        self.assertEqual(len(response.json['categories']), 1)

    def test_indemnities_grouped_by_category_top5_should_have_5_categories(self):
        IndemnityFactory.create_batch(40)
        response = self.client.get("/api/indemnities/categories/?top=5")
        self.assertIn('categories', response.json)
        self.assertEqual(len(response.json['categories']), 5)

    def test_indemnities_grouped_by_category_n_deputies_should_have_one_category_with_deputies(self):
        response = self.client.get('/api/indemnities/categories/deputies/')
        categories = response.json['categories']
        self.assertEqual(len(categories), 1)
        for name, category in categories.items():
            self.assertTrue(len(category['deputies']) > 1)

    def test_indemnities_grouped_by_category_n_deputies_should_have_total_budget_on_deputies(self):
        response = self.client.get('/api/indemnities/categories/deputies/')
        deputy = response.json['categories']['Single Category']['deputies'][0]
        self.assertTrue(set(['name', 'party', 'total_budget']).issubset(deputy.keys()))

    def test_indemnities_grouped_by_category_n_deputies_top5_should_have_5_deputies_per_category(self):
        response = self.client.get(
            '/api/indemnities/categories/deputies/?top=5')
        deputies = response.json['categories']['Single Category']['deputies']
        self.assertEqual(len(deputies), 5)
