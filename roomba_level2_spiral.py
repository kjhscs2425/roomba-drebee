# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed, tracer, update
import room

tracer(0,0)
# # Make the turtle go faster
# speed(7)

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)

###
# Start your code here
 
# each square is 40 pixels x 40 pixels
square = 40

height = 15
width = 20

forward((height - 1)*square)
for i in range(1, min(height, width) + 1):
    vertical_arm_length = (height - i) * square
    horizontal_arm_length = (width - i) * square
    left(90)
    forward(horizontal_arm_length)
    left(90)
    forward(vertical_arm_length)
 
# End your code here
###
 
update()
window.exitonclick()