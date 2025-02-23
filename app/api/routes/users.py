from flask import jsonify, request
from app.api import api

@api.route('/users', methods=['GET'])
def get_users():
    pass

@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    pass

@api.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    pass

@api.route('/users/profile', methods=['GET'])
def get_profile():
    pass

@api.route('/users/profile', methods=['PUT'])
def update_profile():
    pass
