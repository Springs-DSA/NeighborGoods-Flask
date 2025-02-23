from flask import jsonify, request
from app.api import api

@api.route('/notifications', methods=['GET'])
def get_notifications():
    pass

@api.route('/notifications/<int:id>/read', methods=['PUT'])
def mark_notification_read(id):
    pass

@api.route('/notifications/<int:id>', methods=['DELETE'])
def delete_notification(id):
    pass

@api.route('/notifications/unread/count', methods=['GET'])
def get_unread_count():
    pass
