import decimal
from decimal import Decimal 
from PIL import Image 
import time 

# Creating a blank dark screen
image = Image.new(mode="RGB", size = (250,250), color= (0,0,0))
decimal.getcontext().prec = 7 # Used for timing, up to 7 decimal places

"""
The following function will draw a line at the two coordinates:
(x0,y0) and (x1, y1). This is Bresenham's Line Drawing Algorithm.
"""
def draw_bresenham_line(x0,y0,x1,y1):
    total_time = 0 # Calculate the run time for the critical loop

    # If x0 == x1, in other words, it's a vertical line, just draw a vertical line |y1 - y0| times.
    if x0 == x1:
        smaller_y_value = min(y0,y1)
        start = Decimal(time.time())
        for i in range(abs(y0 - y1) + 1):
            image.putpixel((x0, smaller_y_value + i), (255,255,255))
        end = Decimal(time.time())
        total = end - start
        total_time += total
        return total_time

    # If Δx >= Δy, or |x1-x0| >= |y1-y0|, draw horizontally |x1-x0| times.
    elif (abs(x1 - x0)) >= (abs(y1-y0)):
        # If x0 > x1, switch two coordinates so we can draw starting with the smaller x value
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        delta_y = abs(y1 - y0)
        delta_x = abs(x1 - x0)
        big_e = 2 * delta_y - delta_x
        increment1 = 2 * delta_y
        increment2 = 2 * (delta_y - delta_x)
        y_value = y0 # Y value for the critical loop
        x_value = x0 # X value for the critical loop
        slope = (y1- y0) / (x1 - x0)
        max_x_value = max(x0,x1)
        start = Decimal(time.time())

        # The critical loop
        while True:
            image.putpixel((x_value, y_value), (255,255,255))
            if big_e < 0:
                big_e += increment1
            else:
                if slope >= 0: # Increment y value if slope is positive, otherwise decrement
                    y_value += 1
                else: 
                    y_value -= 1
                big_e += increment2
            x_value += 1
            if x_value > max_x_value:
                break
        end = Decimal(time.time())
        total = end - start # Total run time of the critical loop
        total_time += total
        return total_time
      
    # If Δx < Δy, or |x1-x0| < |y1-y0|, draw vertically |y1-y0| times.
    elif (abs(x1-x0)) < (abs(y1-y0)):
        # If y0 > y1, switch two coordinates so we can draw starting with the smaller y value
        if y0 > y1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        delta_y = abs(y1 - y0)
        delta_x = abs(x1 - x0)
        big_e = 2 * delta_x - delta_y
        increment1 = 2 * delta_x
        increment2 = 2 * (delta_x - delta_y)
        y_value = y0 # Y value for the critical loop
        x_value = x0 # X value for the critical loop
        slope = (y1-y0) / (x1 - x0)
        start = Decimal(time.time())
        max_y_value = max(y0,y1)

        # The critical loop
        while True:
            image.putpixel((x_value, y_value), (255,255,255))
            if big_e < 0:
                big_e += increment1
            else:
                if slope >= 0: # Increment y value if slope is positive, otherwise decrement
                    x_value += 1
                else: 
                    x_value -= 1
                big_e += increment2
            y_value += 1
            if y_value > max_y_value:
                break
        end = Decimal(time.time())
        total = end - start # Total run time of the critical loop
        total_time += total
        return total_time

# Save the image and put it in a folder called "Line Results" and name it "bresenham_lines.png"
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
        total_time += draw_bresenham_line(x0, y0, x1, y1) 
    print(f"Bresenham Line Algorithm total run time: {total_time} seconds")
    image.save("Line Results\\bresenham_lines.png")

# Display the image to the screen
def show_image():
    image.show()

# This piece of code is for debugging/testing purposes. (Uncomment as needed)
"""
def manual_draw(x0,y0,x1,y1):
    draw_bresenham_line(x0,y0,x1,y1)
manual_draw(125, 50, 125, 100)
image.show()
"""