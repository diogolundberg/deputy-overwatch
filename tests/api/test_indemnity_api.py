from test_base import BaseTestCase


class IndemnityApiTests(BaseTestCase):


    def test_should_respond_a_json(self):
        response = self.client.get('/api/indemnity')
        self.assertEquals(response.json, dict(success=True))
