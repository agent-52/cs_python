import sys
from PIL import Image
from PIL import ImageOps
from sklearn.utils import resample

if len(sys.argv)>3:
  sys.exit("to many arguments")
elif len(sys.argv)<3:
  sys.exit("too few arguments")

input = sys.argv[1]
output = sys.argv[2]




try:
  image = open(sys.argv[1])
except:
  sys.exit("input does not exist")

shirt = Image.open("shirt.png")
size = shirt.size
print(size)

image = Image.open(sys.argv[1])
ImageOps.fit(image, size, method=Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

image.paste(shirt, shirt)

image.save(output)




