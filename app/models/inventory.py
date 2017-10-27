from pg import createDB
from sqlalchemy.dialects.postgresql import JSON

class Inventory(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.Integer, nullable=False)
    store = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

def __init__(self, sku, store, quantity):
    self.sku = sku
    self.store = store
    self.quantity = quantity

def __repr__(self):
    return '<id {}>'.format(self.id)
