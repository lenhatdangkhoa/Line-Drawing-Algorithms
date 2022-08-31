from PIL import Image # Python Imaging Library

# Creating a blank dark screen
image = Image.new(mode="RGB", size = (500, 500), color = (0,0,0))

for i in range(200):
    image.putpixel((250,i), (255,255,255))
    image.putpixel((250 + i, 200), (255,255,255))


with open("coordinates.txt", 'w') as filename:
    for i in range(10):
        filename.write(f"{i}\n")
image.show()