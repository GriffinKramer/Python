import pygame
from math import pi
import math
x = 330
y = 400
a = 200
b = 400
c = 0
d = 50
s = 100
t = 110

pygame.init()
 

BLACK = (  0,   0,   0)
BLUE =  (  0,   0, 255)
PURPLE = ( 187, 149, 229)
i = 50
 
size = [1000, 500]
screen = pygame.display.set_mode(size)
 

done = False
clock = pygame.time.Clock()
 
while not done:
 
   
    clock.tick(10)
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True
 
    screen.fill(BLACK)
    
    pygame.draw.line(screen, BLUE, (820, 100), (820, 475), 5)
    pygame.draw.line(screen, BLUE, (840, 100), (840, 475), 5)
    pygame.draw.line(screen, BLUE, (860, 100), (860, 475), 5) 
    pygame.draw.line(screen, BLUE, (880, 100), (880, 475), 5)
    pygame.draw.line(screen, BLUE, (900, 100), (900, 475), 5) 
    pygame.draw.line(screen, BLUE, (920, 180), (920, 475), 5) 
    pygame.draw.line(screen, BLUE, (940, 300), (940, 475), 5)    
    pygame.draw.line(screen, BLUE, (960, 380), (960, 475), 5)
    pygame.draw.line(screen, BLUE, (800, 130), (900, 130), 5) 
    pygame.draw.line(screen, BLUE, (800, 190), (920, 190), 5) 
    pygame.draw.line(screen, BLUE, (800, 250), (930, 250), 5) 
    pygame.draw.line(screen, BLUE, (800, 310), (940, 310), 5)
    pygame.draw.line(screen, BLUE, (800, 370), (960, 370), 5) 
    pygame.draw.line(screen, BLUE, (800, 430), (970, 430), 5)  
    pygame.draw.polygon(screen, BLUE, [(800, 100), (900, 100), (980, 475), (800, 475)], 5 )
    
    pygame.draw.circle(screen, BLUE,(300, 200), 50)
    pygame.draw.line(screen, BLUE,(300, 250), (300, 400), 5)
    pygame.draw.line(screen, BLUE,(300, 400), (360, 410), 5)    
    pygame.draw.line(screen, BLUE,(360, 410), (350, 475), 5)

   
    pygame.draw.line(screen, BLUE,(300, 300), (240, 320), 5)
    pygame.draw.line(screen, BLUE,(240, 320), (235, 360), 5)    
    pygame.draw.line(screen, BLUE,(300, 300), (350, 320), 5)
    pygame.draw.line(screen, BLUE,(350, 320), (375, 250), 5)     
    
    a = a + 8.8
    b = math.cos(b) + 480
    if (a>= 450):
        a = 200
        b = 400
    y = y - 3
    x = x + 20
    if (x >= 910):
        x = 330
        y = 400
    pygame.draw.circle(screen, PURPLE, (x, y), 50) 
    pygame.draw.line(screen, BLUE,(300, 400), (a, b), 5)
    
    
    pygame.display.flip()
 

pygame.quit()
