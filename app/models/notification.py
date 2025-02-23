from app import db
from app.models import BaseModel

class Notification(BaseModel):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # return_reminder, request_received, request_status_change, etc.
    content = db.Column(db.Text, nullable=False)
    read = db.Column(db.Boolean, default=False)
    action_url = db.Column(db.String(256))  # Optional URL for notification action
    reference_id = db.Column(db.Integer)  # Optional reference to related entity (request_id, item_id, etc.)
    reference_type = db.Column(db.String(50))  # Type of referenced entity (request, item, etc.)

    def to_dict(self):
        pass

    def from_dict(self, data):
        pass

    def mark_as_read(self):
        pass

    def mark_as_unread(self):
        pass

    @staticmethod
    def create_return_reminder(request_id):
        pass

    @staticmethod
    def create_request_notification(request_id, notification_type):
        pass

    @staticmethod
    def create_item_notification(item_id, notification_type):
        pass

    @classmethod
    def get_unread_count(cls, user_id):
        pass
