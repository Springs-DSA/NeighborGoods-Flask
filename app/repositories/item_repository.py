from app.models import Item
from app.repositories import BaseRepository

class ItemRepository(BaseRepository):
    def __init__(self):
        super().__init__(Item)

    def get_by_owner(self, owner_id):
        pass

    def get_available_items(self):
        pass

    def get_items_by_tag(self, tag):
        pass

    def get_items_by_tags(self, tags):
        pass

    def get_federated_items(self):
        pass

    def get_by_federated_id(self, federated_id):
        pass

    def search_items(self, query):
        pass

    def get_items_available_for_period(self, start_date, end_date):
        pass

    def get_items_with_pending_requests(self):
        pass

    def get_items_with_active_loans(self):
        pass

    def update_availability(self, item_id, available):
        pass

    def update_loan_period(self, item_id, loan_period):
        pass

    def get_popular_items(self, limit=10):
        pass
