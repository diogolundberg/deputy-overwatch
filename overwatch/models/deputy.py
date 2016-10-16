from overwatch import db
from sqlalchemy import Column, Integer, String


class Deputy(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    party = Column(String(255))
    indemnities = db.relationship("Indemnity", back_populates="deputy")

    def __repr__(self):
        return '<Deputy %s: %s (%s)>' % (self.id, self.name, self.party)

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
        yield 'party', self.party