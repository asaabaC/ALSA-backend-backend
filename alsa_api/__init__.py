from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config  # Absolute import

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize your models and controllers
    with app.app_context():
        # Import your models (Make sure you import all models here)
        from .models import user  # Adjust this based on your user model
        
        # Register your blueprints/controllers
        from .controllers.user_controller import auth_bp  # Import the auth blueprint
        app.register_blueprint(auth_bp)  # Register the auth blueprint

    return app
