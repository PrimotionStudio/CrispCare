from app import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    househelp_id = db.Column(db.Integer, db.ForeignKey('househelp.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), default='pending')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'househelp_id': self.househelp_id,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'status': self.status
        }

