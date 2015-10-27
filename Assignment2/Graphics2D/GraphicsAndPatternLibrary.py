'''
Created on Oct 27, 2015

@author: jakenherman
'''

import turtle

turtle = turtle.Turtle()
turtle.speed(3)


def circle(radius = 50, cx = None, cy = None, color = 'black', fill = False):
    
    turtle.penup()
    
    if cx != None or cy != None:
        turtle.goto(int(cx), int(cy))
    

    if color != 'black':
        turtle.pencolor(color)
    
    if fill is True:
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        turtle.getscreen()._root.mainloop() #keep window open until close

    else:
        turtle.pendown()
        turtle.circle(radius)
        
    return

