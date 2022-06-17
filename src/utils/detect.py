from os import listdir

import numpy
from src.utils.mrcnn.utils import Dataset
from os import listdir
from numpy import expand_dims
from numpy import mean
from src.utils.mrcnn.config import Config
from src.utils.mrcnn.model import MaskRCNN
from src.utils.mrcnn.utils import compute_ap
from src.utils.mrcnn.model import load_image_gt
from src.utils.mrcnn.model import mold_image
from matplotlib import pyplot
from matplotlib.patches import Rectangle
import cv2
import os.path
# define the prediction configuration
class PredictionConfig(Config):
	# define the name of the configuration
	NAME = "vegefruit_cfg"
	# number of classes (background + vege)
	NUM_CLASSES = 1 + 1
	# simplify GPU config
	GPU_COUNT = 1
	IMAGES_PER_GPU = 1
# plot a number of photos with ground truth and predictions
def detect(image, model, cfg):
	for i in range(1):	
		# convert pixel values (e.g. center)
		scaled_image = mold_image(image, cfg)
		# convert image into one sample
		sample = expand_dims(scaled_image, 0)
		# make prediction
		yhat = model.detect(sample, verbose=0)[0]
		
		j=0
		# plot each box
		for box in yhat['rois']:
			if j==0:
				# thay duong dan thu muc xuat anh ra
				filename = "test.jpg"
				# get coordinates
				y1, x1, y2, x2 = box
				# calculate width and height of the box
				width, height = x2 - x1, y2 - y1
				crop_img = image[y1:y2, x1:x2]
				cv2.imwrite(filename, crop_img)
			j=j+1

def main():
	try:
		# create config
		cfg = PredictionConfig()
		# define the model
		model = MaskRCNN(mode='inference', model_dir='./', config=cfg)
		# load model weights
		model_path = 'src/utils/mask_rcnn_vegefruit_cfg_0004.h5'
		model.load_weights(model_path, by_name=True)
		img = cv2.imread('test.jpg')
		detect(img, model, cfg)
		return True
	except:
		return False