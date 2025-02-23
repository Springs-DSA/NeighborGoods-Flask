from datetime import datetime

def timeago(date):
    """Convert a datetime to a 'time ago' string."""
    now = datetime.utcnow()
    diff = now - date

    seconds = diff.total_seconds()
    minutes = seconds // 60
    hours = minutes // 60
    days = diff.days

    if days > 30:
        months = days // 30
        if months > 12:
            years = months // 12
            return f"{int(years)} year{'s' if years != 1 else ''} ago"
        return f"{int(months)} month{'s' if months != 1 else ''} ago"
    elif days > 0:
        return f"{int(days)} day{'s' if days != 1 else ''} ago"
    elif hours > 0:
        return f"{int(hours)} hour{'s' if hours != 1 else ''} ago"
    elif minutes > 0:
        return f"{int(minutes)} minute{'s' if minutes != 1 else ''} ago"
    else:
        return "just now"
