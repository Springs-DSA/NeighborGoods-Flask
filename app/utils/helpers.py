import os
import uuid
from datetime import datetime
from flask import current_app, json
from werkzeug.utils import secure_filename

def generate_unique_id():
    """Generate a unique identifier."""
    return str(uuid.uuid4())

def get_file_extension(filename):
    """Get the file extension from a filename."""
    return os.path.splitext(filename)[1]

def generate_unique_filename(original_filename):
    """Generate a unique filename while preserving the original extension."""
    ext = get_file_extension(original_filename)
    return f"{generate_unique_id()}{ext}"

def secure_upload_path(base_path, filename):
    """Create a secure upload path."""
    filename = secure_filename(filename)
    return os.path.join(base_path, filename)

def ensure_directory_exists(directory):
    """Ensure that a directory exists, creating it if necessary."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def format_datetime(dt, format='%Y-%m-%d %H:%M:%S'):
    """Format a datetime object as a string."""
    return dt.strftime(format) if dt else ''

def parse_datetime(dt_str, format='%Y-%m-%d %H:%M:%S'):
    """Parse a datetime string into a datetime object."""
    try:
        return datetime.strptime(dt_str, format)
    except (ValueError, TypeError):
        return None

def sanitize_html(html_content):
    """Sanitize HTML content to prevent XSS attacks."""
    # This is a stub - implement actual HTML sanitization
    return html_content

def truncate_string(text, length=100, suffix='...'):
    """Truncate a string to a specified length."""
    if len(text) <= length:
        return text
    return text[:length].rsplit(' ', 1)[0] + suffix

def format_file_size(size_in_bytes):
    """Format file size in human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.1f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.1f} TB"

def is_valid_json(json_str):
    """Check if a string is valid JSON."""
    try:
        json.loads(json_str)
        return True
    except (ValueError, TypeError):
        return False
