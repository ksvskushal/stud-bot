

from app import db

class Updatelist(db.Model):
    """This class represents the bucketlist table."""

    __tablename__ = 'updatelists'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(2000))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, data):
        """initialize with name."""
        self.data = data[:30]

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Updatelist.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Updatelist: {}>".format(self.data)