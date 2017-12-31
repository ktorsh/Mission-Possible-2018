import turtle
import math
import random
def heading(start, end): #returns the angle of the vector with respect to the relative x-axis
    dx=end[0]-start[0]
    dy=end[1]-start[1]
    if dx==0 and dy>0: #to prevent undefined division in dy/dx
        return 90
    if dx==0 and dy<0:
        return 270
    if dx<0:
        return 180+(math.atan(dy/dx)*180/math.pi)
    else:
        return (math.atan(dy/dx)*180/math.pi)%360

# Acceptable methods...forward, left, right, backward, pos
alex = turtle.Turtle()
target = random.randint(-300, 300),random.randint(-300, 300)

alex.penup()
alex.goto(target)
alex.stamp()  #put a stamp at the randomly chosen target

delta = 20  #distance travelled between testing of location

alex.left(random.randint(0,360))  #randomly choose direction
alex.penup()
alex.goto(random.randint(-300, 300),random.randint(-300, 300))  #random starting location
alex.pendown()
start = alex.pos()
first = True
print(target)
#continue the following loop until your x and y are both within "delta" of the target
while not(target[0] - delta <= start[0] <= target[0] + delta) or not(target[1] - delta <= start[1] <= target[1] + delta):
    alex.forward(delta)
    end = alex.pos()
    alex.left(heading(end,target)-heading(start,end))
    start = alex.pos()

turtle.exitonclick()

