import turtle
import math
import random
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
    #print(start, end)
    a=math.sqrt((target[0]-start[0])**2+(target[1]-start[1])**2)
    #print(a)
    b=math.sqrt((target[0]-end[0])**2+(target[1]-end[1])**2)
    #print(b)
    discrim=((b**2)+(delta**2)-(a**2))/(2*b*delta)
    if discrim>-1: #to account for floating point imprecision, it sometimes goes less than -1
        theta=math.degrees(math.acos(discrim))
    else:
        theta=180 
    print(theta)
    if (abs(end[0]-target[0])/(end[0]-target[0]))==(abs(end[1]-target[1])/(end[1]-target[1])):
        print("first")
        alex.left(180+theta)
    else:
        print("second")
        alex.left(180-theta)
    start = alex.pos()

turtle.exitonclick()
