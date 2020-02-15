'''
Griffin Kramer 
Text Based Adventure game
3rd Period 
Computer Science
2/9/19
'''
import random
key = False
print("Welcome To Griffin's adventure game")
print("The directions you can move are right(r), left(l), foward(f), and backward(b)")
print("When asked if you would like to do an action use (y) for yes and (n) for no")
print("You are stuck in a hotel, and have forgpotten how you got there...")
print("It is dark and you don't know where to go...")
print("You wake up in a bedroom, with a small twin bed and blackout shades")
print("You see a paper with something messely hand written on it")
letter = input("Would you like to read the paper? ")
if letter == 'y':
    print("uif ftdbqf up uif ipufm jt epxo uif tubjst, boe pvu uispvhiu uif epps jo uif ljudifo. gjoe uif lfz jo uif cbuisppn vqtubjst")
hotel = True
while hotel == True:
    dir = input("which way would you like to go? ")
    if dir == 'r':
        print('you can go no further in this direction')
    if dir == 'b':
        print('you walk out onto the balcony, the drop is too far to jump')
        dir = input("which way would you like to go? ")
        while dir == 'r' or  dir == 'l' or  dir == 'f':
            print("You can’t move further in this direction")
            dir = input("which way would you like to go? ")
        if dir == 'b':
            print('you walk back into your hotel room')
    if dir == 'l':
        bath = True
        while bath == True:
            closet = False
            print("you walk into your bathroom")
            print("you see two drawers")
            drawer = input('would you like to open the drawer? ')
            if drawer == 'y':
                if key == False:
                    print("you find a key, this could be usefull later!!!")
                    key = True
                else:
                    print("There is nothing else in the drawer")
            dir = input("which way would you like to go? ")    
            while dir == 'f' or  dir == 'b':
                print("You can’t move further in this direction")
                dir = input("which way would you like to go? ")
            if dir == 'l':
                print("you walk into the closet. There is nothing here for you")
                dir = input("which way would you like to go? ")
                while dir == 'b' or  dir == 'l' or  dir == 'f':
                    print("You can’t move further in this direction")
                    dir = input("which way would you like to go? ")
                if dir == 'r':
                    print('you walk back into the bathroom')
                    dir = input("which way would you like to go? ")
            if dir == 'r':
                print("you walk back into the bedroom")
                bath = False
    if dir == 'f':
        print('You walk out of your room into the hallway')
        print('Your room is at the end of the hallway')
        hall = True
        while hall == True:
            dir = input("which way would you like to go? ")
            while dir == 'f' or dir == 'l':
                print("You can’t move further in this direction")
                dir = input("which way would you like to go? ")
            if dir == 'b':
                print('You walk back into your bedroom')
                hall = False        
            if dir == 'r':
                print("You walk down the hallway and find stairs down to the first floor")
                print("You enter the main lobby")
                lobby = True
                while lobby == True:
                    dir = input("which way would you like to go? ")
                    if dir == 'f':
                        print('you see the doors to exit')
                        print('they are locked, do you have a key?')
                        if key == True:
                            print('you have found the exit')
                            print('Congrats... you escaped the hotel')
                            hotel = False
                            bath = False 
                            hall = False
                            lobby = False
                            dir == 'endgame' 
                    if dir == 'b':
                        lobby = False
                        hall = False
                        print('you see an elevator and get in')
                        print('it takes you back into your bedroom')
                    if dir == 'r':
                        print("You can’t move further in this direction")
                    if dir == 'l':
                        print('you walk back up the stairs, into the hallway')
                        lobby = False




            
            
            
    
