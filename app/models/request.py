from app import db
from app.models import BaseModel

class Request(BaseModel):
    __tablename__ = 'requests'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    requester_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected, completed, cancelled
    request_period = db.Column(db.Integer, nullable=False)  # Requested loan period in days
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    rejection_reason = db.Column(db.Text)
    return_confirmed = db.Column(db.Boolean, default=False)
    return_condition = db.Column(db.Text)
    federated_request_id = db.Column(db.String(256), unique=True)  # ActivityPub ID

    def to_dict(self):
        pass

    def from_dict(self, data):
        pass

    def approve(self):
        pass

    def reject(self, reason=None):
        pass

    def complete(self, return_condition=None):
        pass

    def cancel(self):
        pass

    def is_active(self):
        pass

    def is_overdue(self):
        pass

    def get_duration(self):
        pass
