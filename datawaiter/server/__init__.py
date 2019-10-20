from flask import Flask, jsonify
from flask_restplus import Api

def create_app(env=None):
    from .data import register_routes as register_data_routes

    app = Flask(__name__)
    #app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="Flaskerific API", version="0.1.0")

    register_data_routes(api, app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app