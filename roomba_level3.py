# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import *
import room

# Make the turtle go faster
speed(7)
tracer(0, 0)

# Draw the Level 3 version of the room
window = room.draw_room(level = 3, radius = 5)

###
# Start your code here

square = 40


def fill_rectangle(height, width):
    # go to the middle and face up
    goto(0, 0)
    setheading(90)

    # go to upper left corner of rectangle
    forward(height // 2 * square)
    left(90)
    forward(width // 2 * square)
    # face down
    left(90)
    # draw spiral
    forward((height - 1)*square)
    for i in range(1, min(height, width) + 1):
        vertical_arm_length = (height - i) * square
        horizontal_arm_length = (width - i) * square
        left(90)
        forward(horizontal_arm_length)
        left(90)
        forward(vertical_arm_length)

    # go to the middle and face up
    goto(0, 0)
    setheading(90)

fill_rectangle(11, 1)
fill_rectangle(1, 11)
fill_rectangle(9, 7)
fill_rectangle(7, 9)

 
# End your code here
###
update()
window.exitonclick()