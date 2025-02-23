from flask import current_app, render_template
from flask_mail import Message
from threading import Thread

class EmailService:
    def __init__(self, mail=None):
        self.mail = mail

    def send_async_email(self, msg):
        pass

    def send_email(self, subject, recipients, text_body, html_body=None):
        pass

    def send_password_reset_email(self, user):
        pass

    def send_address_verification_email(self, user):
        pass

    def send_request_notification_email(self, user, request):
        pass

    def send_request_status_update_email(self, user, request):
        pass

    def send_return_reminder_email(self, user, request):
        pass

    def send_item_available_email(self, user, item):
        pass

    def send_welcome_email(self, user):
        pass

    def send_bulk_email(self, recipients, subject, template, **kwargs):
        pass

    def render_email_template(self, template_name, **kwargs):
        pass

    def validate_email_template(self, template_name):
        pass
