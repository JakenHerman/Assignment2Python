'''
Created on Nov 4, 2015

@author: jakenherman
'''

from FurnitureComponents import Room, Sofa, Table

def main():
    
    #rooms
    space = Room(-200, -200, 400, 400, "")
    space.show()
    family_room = Room(-200, 130, 70, 80, "Family")
    family_room.show()
    game_room = Room(-200, -190, 60, 60, "Game Room")
    game_room.show()
    kitchen = Room(100, -200, 75, 90, "Kitchen")
    kitchen.show()
   
    #sofas
    sofa1 = Sofa(0, 0, 40, 40, 'black')
    sofa1.show()
    sofa2 = Sofa(50, 35, 75, 20, 'black')
    sofa2.show()
    
    #tables
    table1 = Table(0, 50, 6, 40, 40, 'red')
    table1.show()
    table2 = Table(100, 100, 4, 40, 50, 'green')
    table2.show()
    
    
    
   
    
    #show sofas
    
    #show tables
    
main()