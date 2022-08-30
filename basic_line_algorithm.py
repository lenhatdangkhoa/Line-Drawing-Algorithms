from PIL import Image

image = Image.new(mode="RGB", size = (500, 500), color = (0,0,0))
for i in range(200):
    image.putpixel((250,i), (255,255,255))
    image.putpixel((250 + i, 200), (255,255,255))
image.show()