from test_base import BaseTestCase


class HomeControllerTests(BaseTestCase):

    def test_should_respond_ok_to_root_path(self):
        response = self.client.get('/')
        self.assert_200(response)
