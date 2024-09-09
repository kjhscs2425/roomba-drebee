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

for _ in range(2):
    forward(square*4)
    left(90)
    forward(square*1)
    left(90)
    forward(square*4)
    right(90)
    forward(square*1)
    right(90)

forward(square*4)
 
# End your code here
###
 
window.exitonclick()