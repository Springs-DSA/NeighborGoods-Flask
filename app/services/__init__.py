class BaseService:
    def __init__(self, repository=None):
        self.repository = repository

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

from app.services.item_service import ItemService
from app.services.request_service import RequestService
from app.services.notification_service import NotificationService
from app.services.email_service import EmailService
from app.services.federation_service import FederationService
from app.services.image_service import ImageService
