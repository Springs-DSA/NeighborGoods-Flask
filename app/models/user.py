from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import BaseModel

class User(UserMixin, BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    address = db.Column(db.String(256))
    address_verified = db.Column(db.Boolean, default=False)
    profile_visibility = db.Column(db.String(20), default='local')
    actor_id = db.Column(db.String(256), unique=True)  # ActivityPub ID

    # Relationships
    items = db.relationship('Item', backref='owner', lazy='dynamic')
    requests_made = db.relationship('Request', backref='requester', lazy='dynamic',
                                  foreign_keys='Request.requester_id')
    notifications = db.relationship('Notification', backref='user', lazy='dynamic')

    def set_password(self, password):
        pass

    def check_password(self, password):
        pass

    def get_reset_password_token(self, expires_in=3600):
        pass

    @staticmethod
    def verify_reset_password_token(token):
        pass

    def to_dict(self):
        pass

    def from_dict(self, data, new_user=False):
        pass
