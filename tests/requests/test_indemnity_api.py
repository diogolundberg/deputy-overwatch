from test_base import BaseTestCase


class IndemnityApiTests(BaseTestCase):

    def test_should_respond_ok_to_indemnities_path(self):
        response = self.client.get("/api/indemnities/")
        self.assert_200(response)

    def test_should_respond_indemnities_in_a_json(self):
        response = self.client.get('/api/indemnities/')
        self.assertEqual('application/json', response.headers['content-type'])
        self.assertIn('indemnities', response.json)

    def test_should_respond_ok_to_categories_parent_path(self):
        response = self.client.get("/api/indemnities/categories/")
        self.assert_200(response)

    def test_should_respond_categories_parent_in_a_json(self):
        response = self.client.get('/api/indemnities/categories/')
        self.assertEqual('application/json', response.headers['content-type'])
        self.assertIn('categories', response.json)

    def test_should_respond_ok_to_categories_deputies_parent_path(self):
        response = self.client.get("/api/indemnities/categories/deputies/")
        self.assert_200(response)

    def test_should_respond_ok_to_categories_deputies_parent_path_with_top(self):
        response = self.client.get("/api/indemnities/categories/deputies/?top=5")
        self.assert_200(response)

    def test_should_respond_422_to_categories_deputies_parent_path_with_invalid_top(self):
        response = self.client.get("/api/indemnities/categories/deputies/?top=injection")
        self.assertStatus(response, 422)

    def test_should_respond_categories_deputies_parent_in_a_json(self):
        response = self.client.get('/api/indemnities/categories/deputies/')
        self.assertEqual('application/json', response.headers['content-type'])
        self.assertIn('categories', response.json)
