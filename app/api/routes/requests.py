from flask import jsonify, request
from app.api import api

@api.route('/requests', methods=['GET'])
def get_requests():
    pass

@api.route('/requests', methods=['POST'])
def create_request():
    pass

@api.route('/requests/<int:id>', methods=['GET'])
def get_request(id):
    pass

@api.route('/requests/<int:id>/status', methods=['PUT'])
def update_request_status(id):
    pass

@api.route('/requests/<int:id>', methods=['DELETE'])
def delete_request(id):
    pass
