import math #Built-in Python Math Library
from PIL import Image # Python Imaging Library
import random # Built-in Python Random Library
# Creating a blank dark screen
image = Image.new(mode="RGB", size = (250, 250), color = (0,0,0))

"""
The following function will draw a line at the two coordinates:
(x0,y0) and (x1, y1). This is a just a basic line drawing algorithm.
"""
def draw_basic_line(x0, y0, x1, y1):
    # If x0 == x1, in other words, it's a vertical line, just draw a vertical line |y1 - y0| times.
    if x0 == x1:
        smaller_y_value = min(y0,y1)
        for i in range(abs(y1 - y0)):
            image.putpixel((x0, smaller_y_value + i), (255,255,255))
  

    # Else, find the equation of the line using two points and draw a line accordingly
    else:
        slope = (y1 - y0) / (x1 - x0)
        y_intercept = y1 - (slope * x1)
        equation = f"y = {slope}x + {y_intercept}" # Equation of the line as the form y = mx + b


        # If Δx >= Δy, or |x1-x0| >= |y1-y0|, draw horizontally |x1-x0| times.
        if (abs(x1 - x0)) >= (abs(y1-y0)):
            smaller_x_value = min(x0, x1)
            for i in range(abs(x1 - x0)):
                x = smaller_x_value + i
                y = (slope * x) + y_intercept
                y = math.trunc(y)
                image.putpixel((x,y), (255,255,255))



        # If Δx < Δy, or |x1-x0| < |y1-y0|, draw vertically |y1-y0| times.
        elif (abs(x1-x0)) < (abs(y1-y0)):
            smaller_y_value = min(y0,y1)
            for i in range(abs(y1-y0)):
               y = smaller_y_value + i
               x = (y - y_intercept)/slope
               x = math.trunc(x)
               image.putpixel((x,y), (255,255,255))




'''
for i in range(20):
    x0 = random.randint(0,250) 
    x1 = random.randint(0,250) 
    y0 = random.randint(0,250) 
    y1 = random.randint(0,250) 
    print(f"x0 = {x0}, y0= {y0}, x1= {x1}, y1 = {y1}")
    draw_basic_line(x0, y0, x1, y1)
    print(f"{x0}, {y0}. {x1}, {y1}")
    image.putpixel((x0,y0), (255,0,0))
    image.putpixel((x1,y1), (255,0,0))
'''
coordinates = []
with open("coordinates.txt", 'r') as f:
    coordinates = f.readlines()

for i in range(len(coordinates)):
    coordinates[i] = int(coordinates[i])
print(coordinates)
line = 0
print(len(coordinates))
for i in range(0, len(coordinates), 4):
    print(f"i = {i}")
    x0 = coordinates[i]
    y0 = coordinates[i + 1]
    x1 = coordinates[i + 2]
    y1 = coordinates[i + 3]
    draw_basic_line(x0, y0, x1, y1)
    print(f"{x0} {y0} {x1} {y1}")

    line += 1
    print(f"Draw {line} lines")

draw_basic_line(126, 245, 193, 34)
image.show()

