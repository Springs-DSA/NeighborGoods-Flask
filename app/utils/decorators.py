from functools import wraps
from flask import abort, current_app
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

def address_verified_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.address_verified:
            abort(403, description="Address verification required")
        return f(*args, **kwargs)
    return decorated_function

def rate_limit(limit=None, per=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Rate limiting logic would go here
            # This is just a stub for now
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def cache_control(*directives):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            response = f(*args, **kwargs)
            response.headers['Cache-Control'] = ', '.join(directives)
            return response
        return decorated_function
    return decorator

def log_activity(activity_type):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Activity logging logic would go here
            # This is just a stub for now
            return f(*args, **kwargs)
        return decorated_function
    return decorator
