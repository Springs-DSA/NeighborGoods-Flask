from app.models import Request
from app.repositories import BaseRepository

class RequestRepository(BaseRepository):
    def __init__(self):
        super().__init__(Request)

    def get_by_requester(self, requester_id):
        pass

    def get_by_item(self, item_id):
        pass

    def get_by_status(self, status):
        pass

    def get_active_requests(self):
        pass

    def get_pending_requests(self):
        pass

    def get_completed_requests(self):
        pass

    def get_overdue_requests(self):
        pass

    def get_requests_by_date_range(self, start_date, end_date):
        pass

    def get_by_federated_id(self, federated_id):
        pass

    def update_status(self, request_id, status):
        pass

    def confirm_return(self, request_id, condition=None):
        pass

    def get_request_history(self, item_id=None, user_id=None):
        pass

    def get_conflicting_requests(self, item_id, start_date, end_date):
        pass
