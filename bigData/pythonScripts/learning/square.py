from swampy.TurtleWorld import *
import math

def square(turtle):
    for info in range(1, 5):
        fd(turtle,  100)
        lt(turtle)

def polygon(t,  n,  length):
    angle = 360 / n
    for i in range(n):
        fd(t,  length)
        lt(t,  angle)

def circle(t,  r):
    #2 * pi * r
    cir = 2 * math.pi * r
    n = 50
    length = cir / n
    polygon(t,  n,  length)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

world = TurtleWorld()
bob = Turtle()
#square (bob)
#polygon(bob,  10,  70)
#circle(bob,  50)
draw(bob,  10,  10)
wait_for_user()
