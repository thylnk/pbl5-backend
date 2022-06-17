import base64
from io import BytesIO
from PIL import Image

def decode(im_b64):
  try: 
    im_bytes = base64.b64decode(im_b64) # im_bytes is a binary image
    im_file = BytesIO(im_bytes) # convert image to file-like object
    img = Image.open(im_file) 
    return img
  except Exception as e:
    print(e)
    return None