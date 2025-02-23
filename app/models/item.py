from app import db
from app.models import BaseModel

class Item(BaseModel):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    tags = db.Column(db.JSON)  # List of strings
    image_path = db.Column(db.String(256))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    available = db.Column(db.Boolean, default=True)
    can_leave_node = db.Column(db.Boolean, default=False)
    loan_period = db.Column(db.Integer)  # Maximum loan period in days
    federated_item_id = db.Column(db.String(256), unique=True)  # ActivityPub ID

    # Relationships
    requests = db.relationship('Request', backref='item', lazy='dynamic')

    def to_dict(self):
        pass

    def from_dict(self, data):
        pass

    def is_available_for_period(self, start_date, end_date):
        pass

    def get_current_request(self):
        pass

    def get_pending_requests(self):
        pass

    def get_request_history(self):
        pass
