from PIL import Image

image = Image.new(mode="RGB", size = (500, 500), color = (0,0,0))
for i in range(50):
    image.putpixel((i,i), (255,255,255))
image.show()