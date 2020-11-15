from app import db

class Volunteers(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    event = db.Column(db.String(100), nullable=False)

    hours = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return f'{self.name} volunteered at {self.event} for {self.hours} hours'

    def __init__(self, name, event, hours):
        self.name = name
        self.event = event
        self.hours = hours
