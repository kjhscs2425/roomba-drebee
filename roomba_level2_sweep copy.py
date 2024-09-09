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

height = 14
width = 19

for _ in range(19 // 2):
    forward(square*height)
    left(90)
    forward(square*1)
    left(90)
    forward(square*height)
    right(90)
    forward(square*1)
    right(90)

for _ in range(width % 2):
    forward(square*height)
    left(90)
    forward(square*1)
    left(90)
    forward(square*height)
 
# End your code here
###
 
update()
window.exitonclick()