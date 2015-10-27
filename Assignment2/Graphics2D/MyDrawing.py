'''
Created on Oct 27, 2015

@author: jaken herman
'''

from Graphics2D import GraphicsAndPatternLibrary

def main():
    GraphicsAndPatternLibrary.circle()
    GraphicsAndPatternLibrary.circle(60, -200, -200, 'blue', True)
    GraphicsAndPatternLibrary.rectangle()
    GraphicsAndPatternLibrary.rectangle(60, 70, 100, 100, 'red', True)
    GraphicsAndPatternLibrary.polygon()
    GraphicsAndPatternLibrary.polygon(70, 45, -200, 200, 6, 'violet', True)
    
    
    return

main()
