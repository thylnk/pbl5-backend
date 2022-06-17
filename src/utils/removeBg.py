import io
import os
from urllib import response

import requests
from flask import Blueprint, jsonify, request
from PIL import Image
from src.utils.decodeBase64 import decode
from src.utils.prediction import run

def remove_background(image):
  image.save('bg.jpg')
  response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('bg.jpg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'Tjd3dCGeTW9gqqKvL5eMvHzF'},
  )
  if response.status_code == requests.codes.ok:
    with open('bg.jpg', 'wb') as out:
      out.write(response.content)
    return True, response.status_code
  else:
    return False, response.status_code
