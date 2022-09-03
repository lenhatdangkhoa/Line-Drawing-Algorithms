import math
from PIL import Image # Python Imaging Library

# Creating a blank dark screen
image = Image.new(mode="RGB", size = (250, 250), color = (0,0,0))

"""
The following function will draw a line at the two coordinates:
(x0,y0) and (x1, y1). This is a just a basic line drawing algorithm.
"""
def draw_basic_line(x0, y0, x1, y1):
    # If x0 == x1, in other words, it's a vertical line, just draw a vertical line |y1 - y0| times.
    if x0 == x1:
        print(True)
        image.putpixel((x0, y0), (255,0,0)) # A red pixel for one endpoint
        for i in range(y1 - y0):
            image.putpixel((x0, y0 + i+ 1), (255,255,255))
        image.putpixel((x0, y1), (255, 0,0)) # Another red pixel for the other endpoint
        image.show()
    # Else, find the equation of the line using two points and draw a line accordingly
    else:
        slope = (y1 - y0) / (x1 - x0)
        y_intercept = y1 - (slope * x1)
        equation = f"y = {slope}x + {y_intercept}" # Equation of the line as the form y = mx + b
        coordinates = [] # The list of the coordinates of the pixels
        for i in range(x1 - x0):
            x = x0 + i
            y = (slope * x) + y_intercept
            y = math.trunc(y)
            image.putpixel((x,y), (255,255,255))
            point = [x, y]
            coordinates.append(point)

        """
        This will write the coordinates to a text file called "coordinates.txt"
        """
        with open("coordinates.txt", 'w') as file:
            for item in coordinates:
                x_y = f"({item[0]}, {item[1]})\n"
                file.write(x_y)
            
        print(f"Equation: {equation}")

   
draw_basic_line(0,0,100,20)
draw_basic_line(0, 0 , 150, 100)
draw_basic_line(0,0, 200, 150)
draw_basic_line(0,0,100,30)

image.show()

