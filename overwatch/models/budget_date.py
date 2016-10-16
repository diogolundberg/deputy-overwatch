from overwatch import db
from overwatch.models import Deputy
from sqlalchemy import Column, ForeignKey, Integer, Date


class BudgetDate(db.Model):
    date = Column(Date, primary_key=True)
    deputy_id = Column(Integer, ForeignKey(Deputy.id), primary_key=True)

    def __repr__(self):
        return '<BudgetDate %s, %s>' % (self.deputy_id, self.date)
