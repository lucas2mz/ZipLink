import uuid
from datetime import datetime
from app import db

class Link(db.Model):
    __tablename__ = "urls"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    original_url = db.Column(db.String, nullable=False)
    short_url = db.Column(db.String, unique=True, nullable=False)
    short_code = db.Column(db.String, unique=True, nullable=False)
    visits = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, original_url: str, short_url: str, short_code: str, visits: int = 0):
        self.original_url = original_url
        self.short_url = short_url
        self.short_code = short_code
        self.visits = visits
