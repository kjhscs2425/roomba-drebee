# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)

###
# Start your code here

# each square is 40 pixels x 40 pixels
square = 40

forward(square*4)
for i in range(4):
    arm_length = (4 - i) * square
    print(arm_length)
    for _ in range(2):
        left(90)
        forward(arm_length)
 
# End your code here
###
 
window.exitonclick()