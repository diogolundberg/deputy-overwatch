from overwatch import db
from overwatch.models import Deputy
from sqlalchemy import Column, ForeignKey, Integer, Date, String


class Indemnity(db.Model):
    deputy_id = Column(Integer, ForeignKey(Deputy.id), primary_key=True)
    date = Column(Date, primary_key=True)
    category_id = Column(Integer, primary_key=True)
    value = Column(String(255))
    category = Column(String(255))

    def __repr__(self):
        return '<Indemnity %s, %s>' % self.date, self.category

    def __iter__(self):
        yield 'date', self.date
        yield 'deputy_id', self.deputy_id
        yield 'category_id', self.category_id
        yield 'category', self.category
        yield 'value', self.value