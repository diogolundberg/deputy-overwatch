from overwatch import db
from overwatch.models import Deputy
from sqlalchemy import Column, ForeignKey, Integer, Date, String


class Indemnity(db.Model):
    deputy_id = Column(Integer, ForeignKey(Deputy.id), primary_key=True)
    date = Column(Date, primary_key=True)
    category_id = Column(Integer, primary_key=True)
    value = Column(String(255))
    category = Column(String(255))
    deputy = db.relationship("Deputy", back_populates="indemnities")

    def __repr__(self):
        return '<Indemnity %s, %s, deputy:%s>' % (self.date.strftime('%d-%m-%Y'), self.category, self.deputy_id)

    def __iter__(self):
        yield 'deputy', dict(self.deputy)
        yield 'category_id', self.category_id
        yield 'date', self.date.strftime('%d-%m-%Y')
        yield 'category', self.category
        yield 'value', self.value