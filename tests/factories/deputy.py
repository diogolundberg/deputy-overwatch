import factory
from overwatch.models import Deputy
from faker import Faker
from random import choice

faker = Faker('pt_BR')

parties = [
    'PR', 'PSDB', 'PP', 'PV', 'PROS', 'PT', 'PRB', 'PSB', 'PSC', 'PDT', 'PTC', 'PTB', 'PSD', 'PPS', 'PC',
    'PEN', 'DEM', 'REDE', 'PHS', 'SEM','PMDB'
]

class DeputyFactory(factory.Factory):
    class Meta:
        model = Deputy

    id = factory.LazyAttribute(lambda x: faker.random_int(min=0, max=9999))
    name = factory.LazyAttribute(lambda x: faker.name())
    party = factory.LazyAttribute(lambda x: choice(parties))
