from app.models import Notification
from app.repositories import NotificationRepository
from app.services import EmailService

class NotificationManager:
    def __init__(self, notification_repository=None, email_service=None):
        self.notification_repository = notification_repository or NotificationRepository()
        self.email_service = email_service or EmailService()

    def create_notification(self, user_id, notification_type, content):
        pass

    def mark_as_read(self, notification_id):
        pass

    def delete_notification(self, notification_id):
        pass

    def get_user_notifications(self, user_id, include_read=False):
        pass

    def get_unread_count(self, user_id):
        pass

    def send_return_reminder(self, request_id):
        pass

    def notify_request_status_change(self, request_id, new_status):
        pass

    def notify_item_available(self, user_id, item_id):
        pass

    def cleanup_old_notifications(self, days_old=30):
        pass

    def bulk_create_notifications(self, notifications_data):
        pass
