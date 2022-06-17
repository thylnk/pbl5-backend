import os

import requests
from flask import Blueprint, jsonify, request
from PIL import Image

from src.utils.decodeBase64 import decode
from src.utils.getCalories import get_by_name
from src.utils.prediction import run
from src.utils.detect import main

image= Blueprint("image", __name__, url_prefix="/api")

@image.post('/image')
def prediction():
  response = {}
  print("Start object detection ...")
  try:
    img64 = request.get_json('data')
    image = decode(img64['data'])
    image.show()
    image.save('test.jpg')
    result = 'error'
    if main():
      result = run()
    response['result'] = result
    rs = get_by_name(result)
    if (rs):
      print(rs.calories)
      response['calories'] = rs.calories
      response['result'] = rs.name
  except Exception:
    response['result'] = 'error'
  return jsonify(response)
