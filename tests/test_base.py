from overwatch import app
from flask.ext.testing import TestCase


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config.Testing')
        return app
