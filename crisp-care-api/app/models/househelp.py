from app import db

class HouseHelp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    services = db.Column(db.String(200), nullable=False)
    availability = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'services': self.services,
            'availability': self.availability,
            'rating': self.rating
        }

