import json
from flask import Blueprint, jsonify

from src.database import Calories
from src.constants.http_status_codes import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR

calories= Blueprint("calories", __name__, url_prefix="/api/calories")

@calories.get('/all')
def get_all():
  resonse = {"status": False}
  try:
    all = Calories.query.all()
    resonse["data"] = []
    for item in all: 
      resonse["data"].append({"id": item.id, "name": item.name, "calories": item.calories, "name1": item.name1})
    resonse["status"] = True
  except Exception as e: 
    print(e)
    return jsonify({"status": False, 'error': e}), HTTP_500_INTERNAL_SERVER_ERROR
  return jsonify(resonse), HTTP_200_OK


@calories.get('/<name>')
def get_by_name(name):
  resonse = {"status": True, "data": None}
  result = Calories.query.filter_by(name=name).first()
  try: 
    if result is not None: 
      resonse["data"]={"calories": result.calories}
    return jsonify(resonse), HTTP_200_OK
  except Exception as e: 
    return jsonify({"status": False, "error": e}), HTTP_500_INTERNAL_SERVER_ERROR