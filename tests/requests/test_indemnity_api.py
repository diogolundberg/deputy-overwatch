from test_base import BaseTestCase


class IndemnityApiTests(BaseTestCase):


    def test_should_respond_ok_to_indemnity_path(self):
        response = self.client.get("/api/indemnity")
        self.assert_200(response)
