from app.models import Item
from app.repositories import ItemRepository
from app.services import NotificationService

class ItemManager:
    def __init__(self, item_repository=None, notification_service=None):
        self.item_repository = item_repository or ItemRepository()
        self.notification_service = notification_service or NotificationService()

    def create_item(self, owner_id, item_data):
        pass

    def update_item(self, item_id, item_data):
        pass

    def delete_item(self, item_id):
        pass

    def get_item(self, item_id):
        pass

    def list_items(self, filters=None):
        pass

    def mark_item_available(self, item_id):
        pass

    def mark_item_unavailable(self, item_id):
        pass

    def validate_loan_period(self, loan_period):
        pass

    def check_item_availability(self, item_id, start_date, end_date):
        pass
