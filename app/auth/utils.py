from functools import wraps
from flask import current_app
from flask_login import current_user
from itsdangerous import URLSafeTimedSerializer

def get_reset_password_token(user, expires_in=3600):
    pass

def verify_reset_password_token(token):
    pass

def send_password_reset_email(user):
    pass

def verify_address_token(token):
    pass

def send_address_verification_email(user):
    pass

def requires_address_verification(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        pass
    return decorated_function
