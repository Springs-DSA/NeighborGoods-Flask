from flask import Blueprint

api = Blueprint('api', __name__)

from app.api.routes import items, requests, users, notifications
