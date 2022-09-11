import random
import basic_line_algorithm as basic
import bresenham_line_algorithm as bresenham
from threading import Thread
from PIL import Image

"""
This is the main module, and it is used for running the program.
When executed, the program asks the users for the number of lines they wish to draw.
Using that number, the random number generator will generate points on the display.
Finally, it will ask the users to display one or both images as a result from the line drawing modules.
"""

number_of_lines = int(input("How many lines do you wish to display? "))
answer = int(input("Please enter \n1 to display basic lines algorithm\n2 to display bresenham lines algorithm\n3 to display both\n-> "))
coordinates = []

# This loop generates random coordinates and put them into a list called "coordinates"
for i in range(number_of_lines):
    x0 = random.randint(0,249) 
    x1 = random.randint(0,249) 
    y0 = random.randint(0,249) 
    y1 = random.randint(0,249)
    points = [f'{x0}',f'{y0}',f'{x1}',f'{y1}']
    coordinates.append(points)

# Add the coordinates to a txt file called "coordinates.txt"
with open("coordinates.txt", 'w') as f:
    for points in coordinates:
        for point in points:
            f.write(point)
            f.write("\n") 

# Pick which line algorithm the users want to display based on their answer
if answer == 1:
    basic.save_image()
    basic.show_image()
elif answer == 2:
    bresenham.save_image()
    bresenham.show_image()
elif answer == 3:
    basic.save_image()
    bresenham.save_image()
    # Create a multi-thread to display both images at once
    try:
        basic_line = Image.open("Line Results\\basic_lines.png")
        bresenham_line = Image.open("Line Results\\bresenham_lines.png")
        thread1 = Thread(target = basic.show_image(), args = (basic_line))
        thread1.start()
        thread2 = Thread(target = bresenham.show_image(), args = (bresenham_line))
        thread2.start()
    except FileNotFoundError:
        print("Cannot display both. <<Files Error>> Please try again.")
else:
    print("Invalid answer. ")

