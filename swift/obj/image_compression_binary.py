#!/usr/bin/python

from PIL import Image
import sys
import os
COMPRESSED_IMAGE_QUALITY = 20

if (len(sys.argv) != 2):
	
	print "Usage: python image_compression.py [jpeg_image_file]"
	sys.exit(1)

if (str(sys.argv[1].split('.')[1]) != 'jpg'):
	
	print "Please provide jpeg file only!"
	sys.exit(1)

image_file = str(sys.argv[1])

# Check if file exists in system
if not (os.path.isfile(image_file)):

	print "File [{0}] does not exist!".format(image_file)

image_name = image_file.split('.')[0]
image_ext = image_file.split('.')[1]

# Convert image into binary file
fh = open(image_file,'rb')
data = fh.read()
fh.close()
data_file = image_name + '.data'
fh = open(data_file,'w')
fh.write(data)
fh.close()

# Load image
img = Image.open(data_file)
size = os.stat(data_file).st_size
print "Original image file [{filename}] size = {size} bytes".format(filename=image_file, size=str(size))

# Save the compressed image
compressed_image_file= "{name}_compressed.{ext}".format(name=image_name, ext=image_ext)
img.save(compressed_image_file, optimize=True, quality=COMPRESSED_IMAGE_QUALITY)
size = os.stat(compressed_image_file).st_size
print "Compressed image file [{filename}] size = {size} bytes".format(filename=compressed_image_file, size=str(size))
