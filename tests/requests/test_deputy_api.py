from test_base import BaseTestCase


class DeputyApiTests(BaseTestCase):


    def test_should_respond_ok_to_deputies_path(self):
        response = self.client.get("/api/deputies/")
        self.assert_200(response)

    def test_should_respond_deputies_in_a_json(self):
        response = self.client.get('/api/deputies/')
        assert 'deputies' in response.json
