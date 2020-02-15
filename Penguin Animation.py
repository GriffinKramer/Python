#Griffin Kramer
#3 Period
#11/29/18
#Penguin Animation
import simplegui
import math
#Variables
x = 160
x2 = 160
x3 = 0
xO = 700
y = 200
yO = 1200
frames = 0 
c = 30
d = 50
lx = -10
ly = 10
#Main Code Drawings 
def draw_penguin(canvas):
    canvas.draw_circle((x, 195), 30, 5, "Black", "Black")
    canvas.draw_polygon([(x - 30, 230), (x + 30, 230), (x + 30 , 365), (x - 30, 365)], 5, 'Black', "Black") 
    canvas.draw_arc((x - 10, 195), 18,0.5 * math.pi , 1.5 * math.pi, 10, 'Orange')
    canvas.draw_polygon([(x + 30, 190), (x + 40, 195), (x + 30,  200)], 10, 'Orange')
    canvas.draw_polygon([(x - 20, 230), (x + 25, 230), (x + 25 , 360), (x - 20, 360)], 5, 'White', "White") 
    canvas.draw_polygon([(x - 10, 230), (x + 20, 230), (x + 20 , 305), (x - 10, 305)], 5, 'White', "Orange") 
    canvas.draw_circle((x - 15, 375), 10, 5, 'Black', 'Black')
    canvas.draw_circle((x + 15, 375), 10, 5, 'Black', 'Black')
    canvas.draw_circle((x + 35, 275), 10, 5, 'Black', 'Black')
    canvas.draw_circle((x - 35, 275), 10, 5, 'Black', 'Black')
    canvas.draw_circle((x + 55, 279), 10, 5, 'Black', 'Black')
    canvas.draw_circle((x - 55, 279), 10, 5, 'Black', 'Black')
    
def draw_iceberg(canvas):
    canvas.draw_polygon([(0, 170), (400, 155), (380, 180), (600, 300), (600, 600), (0, 600)], 5, 'White', 'LightCyan')

def draw_swimming(canvas):
    canvas.draw_circle((x2 + 215, 380), 30, 5, "Black", "Black")
    canvas.draw_polygon([(x2 + 30 , 350), (x2 + 185, 350), (x2 + 185 , 410), (x2 + 30, 410)], 5, 'Black', "Black") 
    canvas.draw_arc((x2 + 205, 380), 18,0.5 * math.pi , 1.5 * math.pi, 10, 'Orange')
    canvas.draw_polygon([(x2 + 245, 375), (x2 + 255, 380), (x2 + 245,  385)], 10, 'Orange')
    canvas.draw_polygon([(x2 + 40, 360), (x2 + 170, 360), (x2 + 170 , 405), (x2 + 40, 405)], 5, 'White', "White") 
    canvas.draw_polygon([(x2 + 95, 370), (x2 + 170, 370), (x2 + 170 , 400), (x2 + 95, 400)], 5, 'White', "Orange") 
    canvas.draw_circle((x2 + 20, 395), 10, 5, 'Black', 'Black')
    canvas.draw_circle((x2 + 20, 365), 10, 5, 'Black', 'Black')
    canvas.draw_circle((x2 + 103, 320), 10, 5, 'Black', 'Black')
    canvas.draw_circle((x2 + 107, 340), 10, 5, 'Black', 'Black')
    canvas.draw_circle((x2 + 107, 415), 10, 5, 'Black', 'Black')
    canvas.draw_circle((x2 + 103, 435), 10, 5, 'Black', 'Black')
    
def draw_octo(canvas):
    canvas.draw_circle((xO, yO), 100, 5, 'Purple', 'Purple') 
    canvas.draw_arc((xO - 100, yO + 100), 100 ,0.5 * math.pi , 1.5 * math.pi, 10, 'Purple')
    canvas.draw_arc((xO - 70, yO + 130), 100 ,0.5 * math.pi , 1.5 * math.pi, 10, 'Purple')
    canvas.draw_arc((xO + 100, yO + 100), 100 ,1.5 * math.pi , 0.5 * math.pi, 10, 'Purple')
    canvas.draw_arc((xO + 70, yO + 130), 100 ,1.5 * math.pi , 0.5 * math.pi, 10, 'Purple')
    canvas.draw_circle((xO - 50, yO), 10, 5, 'White', 'White')
    canvas.draw_circle((xO + 50, yO), 10, 5, 'White', 'White')
    canvas.draw_line((xO - 70, yO - 50), (670, yO), 5,'White')
    canvas.draw_line((xO + 70, yO - 50), (730, yO), 5,'White')

def draw_octo2(canvas):    
    canvas.draw_circle((550, 275), 100, 5, 'Purple', 'Purple') 
    canvas.draw_arc((450, 375), 100 ,0.5 * math.pi , 1.5 * math.pi, 10, 'Purple')
    canvas.draw_arc((480, 405), 100 ,0.5 * math.pi , 1.5 * math.pi, 10, 'Purple')
    canvas.draw_arc((650, 375), 100 ,1.5 * math.pi , 0.5 * math.pi, 10, 'Purple')
    canvas.draw_arc((620, 405), 100 ,1.5 * math.pi , 0.5 * math.pi, 10, 'Purple')
    #canvas.draw_circle((500, 275), 10, 5, 'White', 'White')
    canvas.draw_circle((600, 260), 10, 5, 'White', 'White')
    canvas.draw_arc([625, 290], 50, 0.5*math.pi, math.pi, 5, 'White')
   
def draw_clouds(canvas):
    canvas.draw_circle((c , d), 30, 1, 'White', 'White')
    canvas.draw_circle((c + 50, d), 30, 1, 'White', 'White')
    canvas.draw_circle((c + 100, d), 30, 1, 'White', 'White')
    canvas.draw_circle((c + 30, d + 40), 30, 1, 'White', 'White')
    canvas.draw_circle((c + 80, d + 40), 30, 1, 'White', 'White')
    
def draw_bird(canvas):
    canvas.draw_line((lx, ly), (lx + 55, 40), 5, 'Black')
    canvas.draw_line((lx + 55, 40), (lx + 65, 70), 5, 'Black')
    canvas.draw_line((lx + 65, 70), (lx + 75, 40), 5, 'Black')                
    canvas.draw_line((lx + 75, 40), (lx + 130, ly), 5, 'Black')
    
#Start
def draw_handler(canvas):
    global frames
    global c
    global d 
    
    frames = frames + 1
    if frames < 850:
        draw_iceberg(canvas)
        draw_penguin(canvas)
        waves = 660
        canvas.draw_polygon([(600, 450), (900, 450), (900, 600), (600, 600)], 5, 'Blue', 'Blue')
        for i in range (4):
            canvas.draw_circle((waves, 450), 60, 5, 'Blue', 'LightSkyBlue')
            waves = waves + 120
        canvas.draw_polygon([(600, 450), (600, 300), (900, 300), (900, 450)], 5, 'LightSkyBlue', 'LightSkyBlue')   
        c = 100
        for g in range (3):
            draw_clouds(canvas)
            c = c + 300
            
#Second Frame            
        global x
        global x3
        global y 
        global yO
        global x2
        global lx
        global ly
        x = x + 1
        if x > 550:
            canvas.draw_polygon([(0,0),(900,0),(900,600),(0,600)],1, 'Blue','Blue' )
            draw_swimming(canvas)
        
            x3 = x3 + 3
            if x3 > 50:
                x3 = 0 
            y = y - 0.5 
            if y < 180:
                y = 200
            yO = yO - 3
            if yO <= 300:
                yO = 300
            canvas.draw_circle ((x3, y), 60, 5, 'Blue', 'lightSkyBlue') 
            canvas.draw_circle ((x3 + 120, y), 60, 5, 'Blue', 'lightSkyBlue')            
            canvas.draw_circle ((x3 + 240, y), 60, 5, 'Blue', 'lightSkyBlue')        
            canvas.draw_circle ((x3 + 360, y), 60, 5, 'Blue', 'lightSkyBlue')        
            canvas.draw_circle ((x3 + 480, y), 60, 5, 'Blue', 'lightSkyBlue')        
            canvas.draw_circle ((x3 + 600, y), 60, 5, 'Blue', 'lightSkyBlue')
            canvas.draw_circle ((x3 + 720, y), 60, 5, 'Blue', 'lightSkyBlue')        
            canvas.draw_circle ((x3 + 840, y), 60, 5, 'Blue', 'lightSkyBlue')
            canvas.draw_polygon([(0, y - y), (900, y - y), (900, y),  (0, y)], 1, 'lightSkyBlue', 'lightSkyBlue')
            draw_octo(canvas)
#Third Frame            
        
    elif frames > 850 and frames < 1025:
        canvas.draw_polygon([(0, 0), (900, 0), (900, 600), (0, 600)], 1, 'Lavender', 'Lavender')
        canvas.draw_polygon([(450, 500), (400, 300), (500, 300)], 5, 'Black', 'Peru')
        canvas.draw_circle ((450, 250), 75, 5, 'Black', 'IndianRed')
        canvas.draw_text('AHA!', (100, 100), 50, 'Gold')
        canvas.draw_text('Ice Cream', (650, 100), 50, 'Gold')
#Fourth Frame

    elif frames > 1025 and frames <1200:
        x3 = x3 + 3
        if x3 > 50:
            x3 = 0 
        y = y - 0.5 
        if y < 180:
            y = 200
        lx = lx + 5
        ly = ly + 1
        if ly > 60:
            ly = 10
        
        canvas.draw_polygon([(0,0),(900,0),(900,600),(0,600)],1, 'Blue','Blue' )
        canvas.draw_circle ((x3, y), 60, 5, 'Blue', 'lightSkyBlue') 
        canvas.draw_circle ((x3 + 120, y), 60, 5, 'Blue', 'lightSkyBlue')            
        canvas.draw_circle ((x3 + 240, y), 60, 5, 'Blue', 'lightSkyBlue')        
        canvas.draw_circle ((x3 + 360, y), 60, 5, 'Blue', 'lightSkyBlue')        
        canvas.draw_circle ((x3 + 480, y), 60, 5, 'Blue', 'lightSkyBlue')        
        canvas.draw_circle ((x3 + 600, y), 60, 5, 'Blue', 'lightSkyBlue')
        canvas.draw_circle ((x3 + 720, y), 60, 5, 'Blue', 'lightSkyBlue')        
        canvas.draw_circle ((x3 + 840, y), 60, 5, 'Blue', 'lightSkyBlue')
        canvas.draw_polygon([(0, y - y), (900, y - y), (900, y),  (0, y)], 1, 'lightSkyBlue', 'lightSkyBlue')
        draw_octo(canvas)
        draw_swimming(canvas)
        canvas.draw_polygon([(700, 450), (725, 375), (675, 375)], 5, 'Black', 'Peru')
        canvas.draw_circle ((700, 360), 30, 5, 'Black', 'IndianRed')
        draw_bird(canvas)
#Fith Frame
        
    elif frames >= 1200:
        x2 = 50
        x3 = x3 + 3
        if x3 > 50:
            x3 = 0 
        y = y - 0.5 
        if y < 180:
            y = 200
        canvas.draw_polygon([(0,0),(900,0),(900,600),(0,600)],1, 'Blue','Blue' )
        canvas.draw_circle ((x3, y), 60, 5, 'Blue', 'lightSkyBlue') 
        canvas.draw_circle ((x3 + 120, y), 60, 5, 'Blue', 'lightSkyBlue')            
        canvas.draw_circle ((x3 + 240, y), 60, 5, 'Blue', 'lightSkyBlue')        
        canvas.draw_circle ((x3 + 360, y), 60, 5, 'Blue', 'lightSkyBlue')        
        canvas.draw_circle ((x3 + 480, y), 60, 5, 'Blue', 'lightSkyBlue')        
        canvas.draw_circle ((x3 + 600, y), 60, 5, 'Blue', 'lightSkyBlue')
        canvas.draw_circle ((x3 + 720, y), 60, 5, 'Blue', 'lightSkyBlue')        
        canvas.draw_circle ((x3 + 840, y), 60, 5, 'Blue', 'lightSkyBlue')
        canvas.draw_polygon([(0, y - y), (900, y - y), (900, y),  (0, y)], 1, 'lightSkyBlue', 'lightSkyBlue')
        draw_swimming(canvas)
        draw_octo2(canvas)
        if frames > 1300:
            canvas.draw_text('The End', (350, 100), 50, 'Black')

  
        
#End        
frame = simplegui.create_frame('Testing', 900, 600)
frame.set_canvas_background("LightSkyBlue")
frame.set_draw_handler(draw_handler)
frame.start()