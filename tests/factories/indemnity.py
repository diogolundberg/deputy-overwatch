import factory
from overwatch import db
from overwatch.models import Indemnity
from faker.providers.date_time import Provider
from faker import Faker


fake = Faker('pt_BR')
fake.add_provider(Provider)

class IndemnityFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Indemnity
        sqlalchemy_session = db.session

    deputy_id = factory.LazyAttribute(lambda x: fake.random_int(min=0, max=9999))
    category_id = factory.LazyAttribute(lambda x: fake.random_int(min=0, max=9999))
    date = factory.LazyAttribute(lambda x: fake.date())
    value = factory.LazyAttribute(lambda x: fake.numerify(text="####,#"))
    category = factory.LazyAttribute(lambda x: fake.job())

