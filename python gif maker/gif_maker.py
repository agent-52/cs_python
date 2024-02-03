from PIL import Image
import sys

images = []

image_input_list = []

while True:
 image1 = input("Choose image for making the gif :- ")
 if image1 != "no more":
  image1 = image1 + ".jpeg"
  image_input_list.append(image1)
 else:
  break


for image_input in image_input_list:
 image = Image.open(image_input)
 images.append(image)

if len(images) == 3:
 images[0].save(
 "your_custom.gif", save_all=True, append_images=[images[1], images[2]], duration=200, loop=0
  )
 print("Your Gif is ready Hurray!! it's saved as your_custom.gif")

elif len(images) == 2:
 images[0].save(
  "your_custom.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
 )
 print("Your Gif is ready Hurray!! it's saved as your_custom.gif")
 





