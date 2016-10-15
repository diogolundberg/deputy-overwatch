from overwatch import app, db
from flask.ext.testing import TestCase


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config.Testing')
        db.create_all()
        return app
