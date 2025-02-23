from flask import jsonify, request
from app.api import api

@api.route('/items', methods=['GET'])
def get_items():
    pass

@api.route('/items', methods=['POST'])
def create_item():
    pass

@api.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    pass

@api.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    pass

@api.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    pass
