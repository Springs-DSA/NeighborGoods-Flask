from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
mail = Mail()

login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
login.login_message_category = 'info'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)

    # Register blueprints
    from app.routes import main
    from app.auth import auth
    from app.api import api

    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(api, url_prefix='/api')

    # Register error handlers
    from app.utils import errors
    app.register_error_handler(404, errors.not_found_error)
    app.register_error_handler(500, errors.internal_error)

    # Register template filters
    from app.utils import filters
    app.jinja_env.filters['timeago'] = filters.timeago

    # Add context processor for template variables
    from datetime import datetime
    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}

    # Register shell context
    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User': User,
            'Item': Item,
            'Request': Request,
            'Notification': Notification
        }

    return app

from app.models import User, Item, Request, Notification
