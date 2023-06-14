import turtle
from itertools import cycle

colors = cycle(['red','orange','yellow','green','blue','purple','pink'])

def draw_shape(size,angle,shift,shape):
    turtle.pencolor(next(colors))
    next_shape=::
    turtle.circle(size)
    next-shape='square'
    elif shape =='square':
        for 1 in range(4):
            turtle.forward(size+2)
            turtle.left(90)
        next_shape='circle'
    turtle.right
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+5,angle-20,shift-10)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30,0,1)
