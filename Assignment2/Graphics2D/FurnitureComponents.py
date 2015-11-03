'''
Created on Nov 1, 2015

@author: jakenherman
'''

from Graphics2D import GraphicsAndPatternLibrary

class Room:
    x = float(0)
    y = float(0)
    length = float(0)
    width = float(0)
    name = None
    
    def __init__(self):
        pass
    
    @staticmethod
    def Room(x, y, l, w, n):
        Room.setX(x)
        Room.setY(y)
        Room.setLength(Room().length)
        Room.setWidth(Room().width)
        Room.setName(Room().name)
        
        GraphicsAndPatternLibrary.MyTurtle.rectangle(l, w, x, y)
        GraphicsAndPatternLibrary.MyTurtle.writeText(x, y, n)
        pass
    
    
    @staticmethod
    def setX(x):
        Room.x = x
        pass
    @staticmethod
    def setY(y):
        Room.y = y
        pass
    @staticmethod
    def setLength(length):
        Room.length = length
        pass
    @staticmethod
    def setWidth(width):
        Room.width = width
        pass
    @staticmethod
    def setName(name):
        Room.name = name
        pass
    @staticmethod
    def show():
        pass
    
    #get methods
    @staticmethod
    def getX():
        return Room.x
        pass
    @staticmethod
    def getY():
        return Room.y
        pass
    @staticmethod
    def getLength():
        return Room.length
        pass
    @staticmethod
    def getWidth():
        return Room.width
        pass
    @staticmethod
    def getName():
        return Room.name
        pass
    
class Table:
    x = 0
    y = 0
    shape = 0
    side1 = 0
    side2 = 0
    color = 'black'
    
    def __init__(self):
        pass
    
    @staticmethod
    def Table(x, y, s, l, w, c):
        pass
    @staticmethod
    def setX(x):
        pass
    @staticmethod
    def setY(y):
        pass
    @staticmethod
    def setShape(shape):
        pass
    @staticmethod
    def setSide1(side1):
        pass
    @staticmethod
    def setSide2(side2):
        pass
    @staticmethod
    def setColor(color):
        pass
    @staticmethod
    def show():
        pass
    
    #get methods later
    @staticmethod
    def getX():
        pass
    @staticmethod
    def getY():
        pass
    @staticmethod
    def getShape():
        pass
    @staticmethod
    def getSide1():
        pass
    @staticmethod
    def getSide2():
        pass
    @staticmethod
    def getColor():
        pass

    
class Sofa:
    x = 0
    y = 0
    length = 0
    width = 0
    color = 'black'
    
    def __init__(self):
        pass
    @staticmethod
    def Sofa(x, y, l, w, c):
        pass
    @staticmethod
    def setX(x):
        pass
    @staticmethod
    def setY(y):
        pass
    @staticmethod
    def setLength(length):
        pass
    @staticmethod
    def setWidth(width):
        pass
    @staticmethod
    def setColor(color):
        pass
    @staticmethod
    def show():
        pass
    
    #get methods
    @staticmethod
    def getX():
        pass
    @staticmethod
    def getY():
        pass
    @staticmethod
    def getLength():
        pass
    @staticmethod
    def getWidth():
        pass
    @staticmethod
    def getColor():
        pass

