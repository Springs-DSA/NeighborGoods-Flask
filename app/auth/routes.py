from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.auth import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    pass

@auth.route('/register', methods=['GET', 'POST'])
def register():
    pass

@auth.route('/logout')
@login_required
def logout():
    pass

@auth.route('/verify-address', methods=['POST'])
@login_required
def verify_address():
    pass

@auth.route('/reset-password-request', methods=['GET', 'POST'])
def reset_password_request():
    pass

@auth.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    pass
