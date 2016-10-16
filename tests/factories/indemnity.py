import factory
import logging
from overwatch import db
from overwatch.models import Indemnity
from faker.providers.date_time import Provider
from faker import Faker
from factories import DeputyFactory
from datetime import datetime


logging.getLogger("factory").setLevel(logging.WARN)
faker = Faker('pt_BR')
faker.add_provider(Provider)


class IndemnityFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Indemnity
        sqlalchemy_session = db.session

    deputy = factory.SubFactory(DeputyFactory)
    category_id = factory.LazyAttribute(
        lambda x: faker.random_int(min=0, max=9999))
    date = factory.LazyAttribute(
        lambda x: datetime.strptime(faker.date(pattern="%Y-%m-%d"), "%Y-%m-%d"))
    value = factory.LazyAttribute(lambda x: faker.numerify(text="####,#"))
    category = factory.LazyAttribute(lambda x: faker.job())
