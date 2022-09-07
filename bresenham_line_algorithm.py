import math
from tkinter import W #Built-in Python Math Library
from PIL import Image # Python Imaging Library
import random # Built-in Python Random Library

# Creating a blank dark screen
image = Image.new(mode="RGB", size = (251,251), color= (0,0,0))

"""
The following function will draw a line at the two coordinates:
(x0,y0) and (x1, y1). This is Bresenham's Line Drawing Algorithm.
"""

def draw_bresenham_line(x0,y0,x1,y1):
    
    # If x0 == x1, in other words, it's a vertical line, just draw a vertical line |y1 - y0| times.
    if x0 == x1:
        smaller_y_value = min(y0,y1)
        for i in range(abs(y1 - y0)):
            image.putpixel((x0, smaller_y_value + i), (255,255,255))

    delta_y = y1 - y0
    delta_x = x1 - x0
    big_e = 2 * delta_y - delta_x
    increment1 = 2 * delta_y
    increment2 = 2 * (delta_y - delta_x)
    y_value = y0 # Y value for the critical loop
    x_value = x0 # X value for the critical loop
    
    while True:
        print(f"[{x_value}, {y_value}]")
        image.putpixel((x_value, y_value), (255,255,255))
        if big_e < 0:
            big_e += increment1
        else:
            y_value += 1
            big_e += increment2
        x_value += 1

        if x_value > x1:
            break

draw_bresenham_line(0,0,8,4)
image.show()
