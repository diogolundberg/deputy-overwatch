from test_base import BaseTestCase
from mock import patch


class IndemnityApiTests(BaseTestCase):


    def test_should_respond_indemnities_in_a_json(self):
        response = self.client.get('/api/indemnity/')
        assert 'indemnities' in response.json
