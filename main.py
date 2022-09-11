import random
import basic_line_algorithm as basic
import bresenham_line_algorithm as bresenham
import decimal
from decimal import Decimal
from PIL import Image # Python Imaging Library

number_of_lines = int(input("How many lines do you wish to display? "))
answer = int(input("Please enter \n1 to display basic lines algorithm\n2 to display bresenham lines algorithm\n3 to display both\n-> "))
coordinates = []

for i in range(number_of_lines):
    x0 = random.randint(0,249) 
    x1 = random.randint(0,249) 
    y0 = random.randint(0,249) 
    y1 = random.randint(0,249)
    points = [f'{x0}',f'{y0}',f'{x1}',f'{y1}']
    coordinates.append(points)

with open("coordinates.txt", 'w') as f:
    for points in coordinates:
        for point in points:
            f.write(point)
            f.write("\n") 

if answer == 1:
    basic.save_image()