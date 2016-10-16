import factory
from overwatch import db
from overwatch.models import Indemnity
from faker.providers.date_time import Provider
from faker import Faker
from factories import DeputyFactory
from datetime import datetime


fake = Faker('pt_BR')
fake.add_provider(Provider)


class IndemnityFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Indemnity
        sqlalchemy_session = db.session

    deputy = DeputyFactory.create()
    deputy_id = factory.LazyAttribute(lambda x: fake.random_int(min=0, max=9999))
    category_id = factory.LazyAttribute(lambda x: fake.random_int(min=0, max=9999))
    date = factory.LazyAttribute(lambda x: datetime.strptime(fake.date(pattern="%Y-%m-%d"), "%Y-%m-%d"))
    value = factory.LazyAttribute(lambda x: fake.numerify(text="####,#"))
    category = factory.LazyAttribute(lambda x: fake.job())

