'''
Created on Oct 27, 2015

@author: jaken herman
'''

from Graphics2D import GraphicsAndPatternLibrary

def main():
    GraphicsAndPatternLibrary.MyTurtle.circle()
    GraphicsAndPatternLibrary.MyTurtle.circle(60, -200, -200, 'blue', True)
    GraphicsAndPatternLibrary.MyTurtle.rectangle()
    GraphicsAndPatternLibrary.MyTurtle.rectangle(60, 70, 100, 100, 'red', True)
    GraphicsAndPatternLibrary.MyTurtle.polygon()
    GraphicsAndPatternLibrary.MyTurtle.polygon(70, 45, -200, 200, 6, 'violet', True)
    
    
    return

main()
