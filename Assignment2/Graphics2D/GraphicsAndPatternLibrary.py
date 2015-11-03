'''
Created on Oct 27, 2015

@author: jakenherman
'''

import turtle

turtle = turtle.Turtle()
turtle.speed(3)

class MyTurtle:
    
    @staticmethod
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
            
    
        else:
            turtle.pendown()
            turtle.circle(radius)
            
        return
    
    @staticmethod
    def rectangle(length = 50, width = 50, x = None, y = None, color = 'black', fill = False):  
        
        turtle.penup()
        
        if x != None or y != None:
            turtle.goto(int(x), int(y))
        
        turtle.pencolor(color)
        turtle.fillcolor(color)
        
        if fill is True:
            turtle.pendown()
            turtle.begin_fill()
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.end_fill()
            
        else:
            turtle.pendown()
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
        
        return
    
    @staticmethod
    def polygon(side = 50, angle = None, xstart = None, ystart = None, numberSides = 3, color = 'black', fill = False):  
        
        turtle.penup()
        
        if angle != None:
            turtle.left(angle)
            
        if xstart != None or ystart != None:
            turtle.goto(int(xstart), int(ystart))
        
        turtle.pencolor(color)
        turtle.fillcolor(color)
        
        if fill is True:
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(side, extent = None, steps = numberSides)
            turtle.end_fill()
            
            if angle != None:
                turtle.right(angle)
            
        
        else:
            turtle.pendown()
            turtle.circle(side, extent = None, steps = numberSides)
            
            if angle != None:
                turtle.right(angle)
        
        return
    
    @staticmethod
    def writeText(x = None, y = None, text = None, color = 'black'):
        turtle.penup()
        turtle.pencolor(color)
        turtle.goto(int(x), int(y))
        turtle.pendown()
        turtle.write(text)
        return