from test_base import BaseTestCase


class IndemnityApiTests(BaseTestCase):


    def test_should_respond_ok_to_indemnity_path(self):
        response = self.client.get("/api/indemnities/")
        self.assert_200(response)

    def test_should_respond_indemnities_in_a_json(self):
        response = self.client.get('/api/indemnities/')
        assert 'indemnities' in response.json

    def test_should_respond_ok_to_categories_parent_path(self):
        response = self.client.get("/api/indemnities/categories/deputies")
        self.assert_200(response)

    def test_should_respond_categories_parent_in_a_json(self):
        response = self.client.get('/api/indemnities/categories/deputies/')
        assert 'categories' in response.json