from glob import glob
from PIL import Image
import os
images = []
image_names = []
for img in glob("./Images/*.jpg"):
	image_names.append(img)
	images.append(Image.open(img))
	
base_image = images[0]
for image in images:
	base_image = Image.blend(base_image, image, 0.6)

base_image_2 = images[-1]
for image in reversed(images): 
	base_image_2 = Image.blend(base_image_2, image, 0.6)

base_image_x = Image.blend(base_image, base_image_2, 0.5)
base_image_y = Image.blend(base_image_2, base_image, 0.5)
base_image_xy = Image.blend(base_image_x, base_image_y, 0.5)
base_image_xy.save(img[9:-8]+'.jpg')


	