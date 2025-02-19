from flask import Flask, session
from controllers import barang_controller

def create_app():
    """Factory function to create and configure the Flask application."""
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    # Register blueprints
    app.register_blueprint(barang_controller)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)