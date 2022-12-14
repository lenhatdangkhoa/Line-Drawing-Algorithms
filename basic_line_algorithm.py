import math 
from PIL import Image
from decimal import Decimal 
import decimal
import time

# Creating a blank dark screen
image = Image.new(mode="RGB", size = (250, 250), color = (0,0,0))
decimal.getcontext().prec = 7 # Used for timing, up to 7 decimal places

"""
The following function will draw a line at the two coordinates:
(x0,y0) and (x1, y1). This is a just a basic line drawing algorithm.
"""
def draw_basic_line(x0, y0, x1, y1):
    total_time = 0 # Calculate the run time for the critical loop

    # If x0 == x1, in other words, it's a vertical line, just draw a vertical line |y1 - y0| times.
    if x0 == x1:
        smaller_y_value = min(y0,y1)
        start = Decimal(time.time())
        # The critical loop
        for i in range(abs(y1 - y0)):
            image.putpixel((x0, smaller_y_value + i), (255,255,255))
        end = Decimal(time.time())
        total = end - start # Total run time of the critical loop
        total_time += total
    # Else, find the equation of the line using two points and draw a line accordingly
    else:
        slope = (y1 - y0) / (x1 - x0)
        y_intercept = y1 - (slope * x1)

        # If Δx >= Δy, or |x1-x0| >= |y1-y0|, draw horizontally |x1-x0| times.
        if (abs(x1 - x0)) >= (abs(y1-y0)):
            smaller_x_value = min(x0, x1)
            start = Decimal(time.time())
            # The critical loop
            for i in range(abs(x1 - x0) + 1):
                x = smaller_x_value + i
                y = (slope * x) + y_intercept
                y = math.trunc(y)
                image.putpixel((x,y), (255,255,255))
            end = Decimal(time.time())
            total = end - start # Total run time of the critical loop
            total_time += total
        # If Δx < Δy, or |x1-x0| < |y1-y0|, draw vertically |y1-y0| times.
        elif (abs(x1-x0)) < (abs(y1-y0)):
            smaller_y_value = min(y0,y1)
            start = Decimal(time.time())
            # The critical loop
            for i in range(abs(y1-y0) +1):
               y = smaller_y_value + i
               x = (y - y_intercept)/slope
               x = math.trunc(x)
               image.putpixel((x,y), (255,255,255))
            end = Decimal(time.time())
            total = end - start # Total run time of the critical loop
            total_time += total
    return total_time

# Save the image and put it in a folder called "Line Results" and name it "basic_lines.png"
def save_image():
    total_time = 0
    coordinates = []
    with open("coordinates.txt", 'r') as f:
        coordinates = f.readlines()
    for i in range(len(coordinates)):
        coordinates[i] = int(coordinates[i])
    for i in range(0, len(coordinates), 4):
        x0 = coordinates[i]
        y0 = coordinates[i + 1]
        x1 = coordinates[i + 2]
        y1 = coordinates[i + 3]
        total_time += draw_basic_line(x0, y0, x1, y1)
    image.save("Line Results\\basic_lines.png")
    print(f"Basic Line Algorithm total run time: {total_time} seconds")

# Display the image to the screen
def show_image():
    image.show()

# This function is for debugging/testing purposes. (Uncomment if needed)
"""
def manual_draw(x0,y0,x1,y1):
    draw_basic_line(x0,y0,x1,y1)
manual_draw(10 ,24, 25, 150)
image.show()
"""