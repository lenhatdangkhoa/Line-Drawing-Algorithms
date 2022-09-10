import math
from multiprocessing.heap import BufferWrapper
from re import X
from tkinter import W #Built-in Python Math Library
from PIL import Image # Python Imaging Library
import random # Built-in Python Random Library

# Creating a blank dark screen
image = Image.new(mode="RGB", size = (250,250), color= (0,0,0))

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

    # If Δx >= Δy, or |x1-x0| >= |y1-y0|, draw horizontally |x1-x0| times.
    if (abs(x1 - x0)) >= (abs(y1-y0)):
        delta_y = abs(y1 - y0)
        delta_x = abs(x1 - x0)
        big_e = 2 * delta_y - delta_x
        increment1 = 2 * delta_y
        increment2 = 2 * (delta_y - delta_x)
        y_value = min(y0, y1) # Y value for the critical loop
        x_value = min(x0,x1) # X value for the critical loop

        while True:

            image.putpixel((x_value, y_value), (255,255,255))
            if big_e < 0:
                big_e += increment1
            else:
                y_value += 1
                big_e += increment2
            x_value += 1

            if x_value > max(x0,x1):
                break

    # If Δx < Δy, or |x1-x0| < |y1-y0|, draw vertically |y1-y0| times.
    elif (abs(x1-x0)) < (abs(y1-y0)):
        if y0 > y1:
            print(f"x0 = {x0} y0 = {y0} x1 = {x1} y1 = {y1}")
            x0, x1 = x1, x0
            y0, y1 = y1, y0
            print(f"x0 = {x0} y0 = {y0} x1 = {x1} y1 = {y1}")
        delta_x = (x1 - x0) * 2
        delta_y = (x1- x0) * 2
        big_e = delta_x - delta_y
        x_value = x0
        y_value = y0
        image.putpixel((x_value, y_value), (255,255,255))
        while (delta_y != 0):
            if big_e >= 0:
                x_value += 1
                big_e -= delta_y
            
            big_e += delta_x
            y_value += 1
            print(f"x = {x_value} y = {y_value}")
            image.putpixel((x_value, y_value), (255,255,255))

coordinates = []
"""
for i in range(1):
    x0 = random.randint(0,249) 
    x1 = random.randint(0,249) 
    y0 = random.randint(0,249) 
    y1 = random.randint(0,249)
    points = [f'{x0}',f'{y0}',f'{x1}',f'{y1}']
    coordinates.append(points)
    draw_bresenham_line(x0, y0, x1, y1)
    image.putpixel((x0,y0), (255,0,0))
    image.putpixel((x1,y1), (255,0,0))
"""
with open("coordinates.txt", 'w') as f:
    for points in coordinates:
        for point in points:
            f.write(point)
            f.write("\n")  
print(coordinates)
#draw_bresenham_line(193, 34, 126, 245)
draw_bresenham_line(193, 34, 126, 245)
image.putpixel((193, 34), (255,0,0))
image.putpixel((126, 245), (255,0,0))
image.show()
