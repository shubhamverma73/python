from PIL import Image

img = Image.open("image.png")
print(img.format) # PNG
print(img.size) # (width, height)
print(img.mode) # RGBA
img.show() # display the image

max_size = (800, 800)
img = img.resize(max_size)  # resize the image to exactly 800x800
#img = img.thumbnail(max_size)  # resize the image to exactly 800x800 if it is larger than 800x800, otherwise keep the original size
print(img.size)  # print size after resizing
img = img.convert('RGB')  # convert to RGB mode for JPEG compatibility
img.save("new_image.jpg") # save the image in a different format