import math #Built-in Python Math Library
from PIL import Image # Python Imaging Library
import random # Built-in Python Random Library
# Creating a blank dark screen
image = Image.new(mode="RGB", size = (251, 251), color = (0,0,0))

"""
The following function will draw a line at the two coordinates:
(x0,y0) and (x1, y1). This is a just a basic line drawing algorithm.
"""
def draw_basic_line(x0, y0, x1, y1):
    # If x0 == x1, in other words, it's a vertical line, just draw a vertical line |y1 - y0| times.
    if x0 == x1:
        print(True)
        smaller_y_value = min(y0,y1)
        for i in range(abs(y1 - y0)):
            image.putpixel((x0, smaller_y_value + i), (255,255,255))
  

    # Else, find the equation of the line using two points and draw a line accordingly
    else:
        slope = (y1 - y0) / (x1 - x0)
        y_intercept = y1 - (slope * x1)
        equation = f"y = {slope}x + {y_intercept}" # Equation of the line as the form y = mx + b
        coordinates = [] # The list of the coordinates of the pixels

        # If Δx >= Δy, or |x1-x0| >= |y1-y0|, draw horizontally |x1-x0| times.
        if (abs(x1 - x0)) >= (abs(y1-y0)):
            smaller_x_value = min(x0, x1)
            for i in range(abs(x1 - x0)):
                x = smaller_x_value + i
                y = (slope * x) + y_intercept
                y = math.trunc(y)
                image.putpixel((x,y), (255,255,255))
                point = [x, y]
                coordinates.append(point)

        # If Δx < Δy, or |x1-x0| < |y1-y0|, draw vertically |y1-y0| times.
        elif (abs(x1-x0)) < (abs(y1-y0)):
            smaller_y_value = min(y0,y1)
            for i in range(abs(y1-y0)):
               y = smaller_y_value + i
               x = (y - y_intercept)/slope
               x = math.trunc(x)
               image.putpixel((x,y), (255,255,255))
               point = [x,y]
               coordinates.append(point)

        """
        This will write the coordinates to a text file called "coordinates.txt"
        """
        with open("coordinates.txt", 'w') as file:
            file.write("x\t|\ty\n")
            for item in coordinates:
                x_y = f"{item[0]}\t|\t{item[1]}\n"
                file.write(x_y)
            
        print(f"Equation: {equation}")

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

image.show()

