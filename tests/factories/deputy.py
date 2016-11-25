import factory
import logging
from overwatch import db
from overwatch.models import Deputy
from faker import Faker
from random import choice


logging.getLogger("factory").setLevel(logging.WARN)
faker = Faker('pt_BR')

parties = [
    'PR', 'PSDB', 'PP', 'PV', 'PROS', 'PT', 'PRB', 'PSB', 'PSC', 'PDT', 'PTC',
    'PTB', 'PSD', 'PPS', 'PC', 'PEN', 'DEM', 'REDE', 'PHS', 'SEM', 'PMDB'
]


class DeputyFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Deputy
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda x: faker.name())
    party = factory.LazyAttribute(lambda x: choice(parties))
