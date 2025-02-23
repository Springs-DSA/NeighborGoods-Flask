from app import db

class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get(self, id):
        pass

    def get_all(self):
        pass

    def create(self, **kwargs):
        pass

    def update(self, id, **kwargs):
        pass

    def delete(self, id):
        pass

    def filter_by(self, **kwargs):
        pass

    def paginate(self, page=1, per_page=20, **kwargs):
        pass

from app.repositories.user_repository import UserRepository
from app.repositories.item_repository import ItemRepository
from app.repositories.request_repository import RequestRepository
from app.repositories.notification_repository import NotificationRepository
