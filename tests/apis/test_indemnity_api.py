from test_base import BaseTestCase
from factories import IndemnityFactory


class IndemnityApiTests(BaseTestCase):
    
    def setUp(self):
        IndemnityFactory.create_batch(10)

    def test_should_return_10_indemnities(self):
        response = self.client.get("/api/indemnities/")
        self.assertEqual(len(response.json['indemnities']), 10)
        
    def test_each_indemnity_in_json_should_have_category_and_value(self):
        response = self.client.get("/api/indemnities/")
        for indemnity in response.json['indemnities']:
            self.assertTrue(set(['category','value']).issubset(indemnity))
