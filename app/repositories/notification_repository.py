from app.models import Notification
from app.repositories import BaseRepository

class NotificationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Notification)

    def get_user_notifications(self, user_id, include_read=False):
        pass

    def get_unread_notifications(self, user_id):
        pass

    def get_notifications_by_type(self, notification_type):
        pass

    def get_notifications_by_reference(self, reference_type, reference_id):
        pass

    def mark_as_read(self, notification_id):
        pass

    def mark_all_as_read(self, user_id):
        pass

    def delete_old_notifications(self, days_old=30):
        pass

    def get_unread_count(self, user_id):
        pass

    def create_return_reminder(self, request_id):
        pass

    def create_request_notification(self, request_id, notification_type):
        pass

    def create_item_notification(self, item_id, notification_type):
        pass

    def bulk_create(self, notifications_data):
        pass
