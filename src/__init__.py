import os

from flask import Flask, jsonify

from src.calories import calories
from src.constants.http_status_codes import (HTTP_404_NOT_FOUND,
                                             HTTP_405_METHOD_NOT_ALLOWED,
                                             HTTP_500_INTERNAL_SERVER_ERROR)
from src.database import db
from src.image import image


def create_app(test_config = None):
  app = Flask(__name__, instance_relative_config = True)

  if test_config is None:
    app.config.from_mapping(
      SECRET_KEY=os.environ.get("SECRET_KEY"),
      SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI"),
      SQLALCHEMY_TRACK_MODIFICATIONS=False,
      PORT = 3000
    )
  
  else:
    app.config.from_mapping(test_config)

  db.app = app
  db.init_app(app)

  app.register_blueprint(image)
  app.register_blueprint(calories)

  @app.errorhandler(HTTP_404_NOT_FOUND)
  def handle_404(e):
    return jsonify({"error": "NOT FOUND"}), HTTP_404_NOT_FOUND

  @app.errorhandler(HTTP_405_METHOD_NOT_ALLOWED)
  def handle_405(e):
    return jsonify({"error": "The method is not allowed for the requested URL"}), HTTP_405_METHOD_NOT_ALLOWED

  @app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
  def handle_500(e):
    return jsonify({"error": "Something went wrong, we are working on it"}), HTTP_500_INTERNAL_SERVER_ERROR

  return app
