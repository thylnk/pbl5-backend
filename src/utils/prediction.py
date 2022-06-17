import base64
import io

import cv2
import numpy as np
import tensorflow as tf
from keras.preprocessing.image import img_to_array, load_img
from PIL import Image
from pyexpat import model

model = tf.keras.models.load_model('./src/utils/Fruits_Classification.model')

categories = ["BapSu", "BiDao", "BiNgo2", "BiNgoi", "Bo", "CaChua", "CaRot", "CaTim", "CuCai", "Dua", "DuaHau", "DuaHau2", "DuaLuoi", "DuDu", "MuopDang", "OtChuongVang", "SuHao", "Tao", "ThanhLong", "Xoai"]

def prepare(filepath):
  img_array = cv2.imread(filepath)
  img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
  new_array = cv2.resize(img_array, (100,100))
  new_array = new_array/255.0
  return new_array.reshape(-1,100,100,3)

def imageCV(img):
  new_array = cv2.resize(img_to_array(img), (100,100))
  new_array = new_array/255.0
  return new_array.reshape(-1,100,100,4)

def run():
  print("start predict")
  img1 = 'test.jpg'
  try: 
    prediction = model.predict([prepare(img1)])
    print(prediction)
    result = str(categories[int(np.argmax(prediction))])
    print('Predicted value: ' + str(np.argmax(prediction)))
    print('Name of fruit: ' + str(categories[int(np.argmax(prediction))]))
    print('Prediction: ' + str(np.max(prediction)))
  except:
    result = 'error'
  return result
