import pygame
import os
import time
#Choice Control Variables
x = 0
y = 0
z = 0
con = 0
choice_headset = 0
story = 0
tcas_choice = 0
hyd = 0
investigate = 0
emergency = 0
jump = 0
#Mouse Click Variables
off = 0
off1 = 0
off2 = 0
off3 = 0
off4 = 0
off5 = 0
off6 = 0
off7 = 0
off8 = 0
off9 = 0
off10 = 0
off11 = 0
off12 = 0
off13 = 0
off14 = 0
c1off = 0
c1go = 0
choice1 = 0
choice2 = 0
choice3 = 0
choice_take_controls = 0
cabin = 0
ct1 = 0
ct2 = 0
ct3 = 0
ct4 = 0
ct5 = 0
ct6 = 0
ct7 = 0
ct8 = 0
ct9 = 0
ct10 = 0
ct11 = 0
box = 0
box2 = 0
#Death A variables
da1 = 0
da2 = 0
endA = 0
offda1 = 0
offda2 = 0
offendA = 0
offendQ = 0
#Death 69 variables
d69 = 0
d70 = 0
offd69 = 0
offd70 = 0
#Story part A variables, on/off for mouse click on/mouse click off
a3a = 0
a3b = 0
a3c = 0
a3d = 0
a2a = 0
a2b = 0
offa3a = 0
offa3b = 0
offa3c = 0
offa3d = 0
offa3e = 0
offa2a = 0
offa2b = 0
offa2c = 0
offa2d = 0

#Story part C variables -
cd1 = 0
cd2 = 0
cd3 = 0
cdo1 = 0
cdo2 = 0
cdo3 = 0
cdo4 = 0

od1 = 0
od2 = 0
od3 = 0
ofod = 0
ofodb = 0
ofodc = 0
ofodd = 0

ctrl = 0
#Color 
story = False
White = (255, 255, 255)
Black = (0, 0, 0)
BLUE =  (  0,   0, 255)
#Death B Variables
deathB_A = 0
deathB_B = 0
deathB_C = 0
deathB_offA = 0
deathB_offB = 0
deathB_offC = 0
deathB_offD = 0

#headset Variables
hs1 = 0
hs2 = 0
hs3 = 0
hs4 = 0
hs5 = 0
hs6 = 0
hs7 = 0
hs8 = 0
hs9 = 0
hs10 = 0
tcas_t = 0
tcas_t2 = 0
tcas_c = 0
tcas_c2 = 0
tcas_c3 = 0
tcas_c4 = 0
tcas_c5 = 0
choice_ctrl =0
choice_headset = 0

#death S variables
D_S1 = 0
D_S2 = 0
D_S3 = 0
D_S4 = 0
D_S5 = 0
D_S6 = 0
#controls ascend
near_miss_off = 0
near_miss_on = 0
hydraulic1_off = 0
hydraulic1_on = 0
Hydaraulic_Jack_not_on = 0
Hydaraulic_Jack_on = 0
go_to_choice_5 = 0
choice5 = 0

#Text control variables from tcas choice in story to story part 5
tcas1 = 0
tcas2 = 0
tcas3 = 0
tcas4 = 0
tcas5 = 0
tcas6 = 0
tcas7 = 0
tcas8 = 0
tcas9 = 0
tcas10 = 0
tcas11 = 0
tcas12 = 0 
tcas13 = 0

#Death, story code: 7B
death7B = 0

#text control variables from choice 5 to choice 6
walk_through_cabin_off = 0
blocking_aisle_on = 0
blocking_aisle_off = 0
shaken_open_on = 0
shaken_open_off = 0
parachute_on = 0
parachute_off = 0
go_to_choice_6 = 0
choice6 = 0

#text control variables from choice 6 to choice 7
explosive_off = 0
now_what_on = 0
now_what_off = 0
go_to_choice_7 = 0
choice7 = 0

#Death C
deathC_control = 0
deathC = 0
smoothie_on = 0
smoothie_off = 0

#game win option
win_off = 0
sucess_on = 0
sucess_off = 0
guard_on = 0
guard_off = 0
saved_on = 0
saved_off = 0
end_control = 0

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def text_box():
    pygame.draw.polygon(screen, Black, [(0, 500), (0, 700), (1000, 700), (1000, 500)])
    
def button1():
    image = (pygame.transform.scale(get_image('closeddoor.jpg'), (1000, 700)))
    screen.blit((image), (0, 0))
#Button formats

def draw_buttons():
    pygame.draw.polygon(screen, White,[(0, 500), (0, 600), (500, 600), (500, 500)], 5)
    pygame.draw.polygon(screen, Black,[(0, 500), (0, 600), (500, 600), (500, 500)])
    pygame.draw.polygon(screen, White,[(500, 500), (500, 600), (1000, 600), (1000, 500)], 5)
    pygame.draw.polygon(screen, Black,[(500, 500), (500, 600), (1000, 600), (1000, 500)])
    pygame.draw.polygon(screen, White,[(0, 600), (0, 700), (500, 700), (500, 600)], 5)
    pygame.draw.polygon(screen, Black,[(0, 600), (0, 700), (500, 700), (500, 600)])
    pygame.draw.polygon(screen, White,[(500, 600), (500, 700), (1000, 700), (1000, 600)], 5)
    pygame.draw.polygon(screen, Black,[(500, 600), (500, 700), (1000, 700), (1000, 600)])

def draw_2buttons():
    pygame.draw.polygon(screen, White,[(0, 500), (0, 600), (1000, 600), (1000, 500)], 5)
    pygame.draw.polygon(screen, Black,[(0, 500), (0, 600), (1000, 600), (1000, 500)])
    pygame.draw.polygon(screen, White,[(0, 600), (0, 700), (1000, 700), (1000, 600)], 5)
    pygame.draw.polygon(screen, Black,[(0, 600), (0, 700), (1000, 700), (1000, 600)])

def onebutton():
    pygame.draw.polygon(screen, White,[(0, 500), (0, 700), (1000, 700), (1000, 500)], 5)
    pygame.draw.polygon(screen, Black,[(0, 500), (0, 700), (1000, 700), (1000, 500)])

#game start image stuff
def start_game_image():
    image = (pygame.transform.scale(get_image('start_game_image.jpg'), (1000, 700)))
    screen.blit((image), (0, 0))
    textsurface = myfont2.render('Welcome to', False, (0, 0, 0))
    screen.blit(textsurface,(700,500))
    text = myfont2.render('[Escape]', False, (0, 0, 0))
    screen.blit(text,(760,550))


def story_start():
    screen.fill(Black)
    text = myfont3.render('You wake up. Groggily opening your eyes, ambient noise of the', False, (White), (0, 0, 0))
    text3 = myfont3.render('gentle engine rumbling surrounds you.', False,(White), (0, 0, 0))
    screen.blit(text,(5,550))
    screen.blit(text3,(5, 600))

def aircraft_cabin():
    image = (pygame.transform.scale(get_image('cabin.jpg'), (1000, 700)))
    screen.blit((image), (0, 0))

#Cabin Text = cabt 
def cabt1():
    text_box()
    text = myfont4.render('You’re sitting in an airliner, with no memory of any recent events.', False, (White), (0, 0, 0))
    text2 = myfont4.render('As you look around and get accustomed to your surroundings, you', False, (White), (0, 0, 0))
    text3 = myfont4.render('realize the source of your unease, the reason for the uncomfortably', False, (White), (0, 0, 0))
    text4 = myfont4.render('clear silence.  There’s no one else on board.', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))
    screen.blit(text3,(5,620))
    screen.blit(text4, (5,660))

def cabt2():
    text_box()
    text = myfont4.render('You: “Wait what’s going on? Who are you? Wait he’s right, where ', False, (White), (0, 0, 0))
    text2 = myfont4.render('the hell is everyone?! Where’s that voice coming from?”', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))

def cabt3():
    text_box()
    text = myfont4.render('You yell into the empty aircraft, the only response the echo of your', False, (White), (0, 0, 0))
    text2 = myfont4.render('own voice through the cabin.', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))

def cabt4():
    text_box()
    text = myfont4.render('You: “Who the hell are you? What’s going on?”', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))

def cabt5():
    text_box()
    text = myfont4.render('You: “What the hell did you do to me?!”', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))


def cabt6():
    text_box()
    text = myfont4.render('You try once again, yelling into the deserted cabin. Little does the', False, (White), (0, 0, 0))
    text2 = myfont4.render('alarmed passenger know, the jetliner, suspended 35,000 above', False, (White), (0, 0, 0))
    text3 = myfont4.render('the Atlantic Ocean, is inhabited by him alone. But to add on to', False, (White), (0, 0, 0))
    text4 = myfont4.render('his troubles even furth-', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))
    screen.blit(text3,(5,620))
    screen.blit(text4, (5,660))


def cabt7():
    text_box()
    text = myfont4.render('You: “What?! There’s no pilot?!”', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))

def cabt8():
    text_box()
    text = myfont4.render('To add on to their troubles even further, a timed explosive was', False, (White), (0, 0, 0))
    text2 = myfont4.render('planted in the tail section of the aircraft. A charge that, when,', False, (White), (0, 0, 0))
    text3 = myfont4.render('detonated in an hour, will cripple the primary control systems of the', False, (White), (0, 0, 0))
    text4 = myfont4.render('airliner.', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))
    screen.blit(text3,(5,620))
    screen.blit(text4, (5,660))
    

def cabt9():
    text_box()
    text = myfont4.render('You:“What the- Please! Why are you doing this?!”', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    
def cabt10():
    text_box()
    text = myfont4.render('You question, screaming, but no one answers.', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))

def cabt11():
    text_box()
    text = myfont4.render('With only their wits to guide them, our valiant hero must find', False, (White), (0, 0, 0))
    text2 = myfont4.render('escape or rescue within an hour, or perish spectacularly trying!', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))


def choice1_button_text():
    text = myfont5.render('Approach flight deck', False, (White), (0, 0, 0))
    text2 = myfont5.render('Approach tail section', False, (White), (0, 0, 0))
    text3 = myfont5.render('Approach aft cabin door', False, (White), (0, 0, 0))
    text4 = myfont5.render('Do nothing. No like literally, just do nothing.', False, (White), (0, 0, 0))
    screen.blit(text,(5,500))
    screen.blit(text2,(505,500))
    screen.blit(text3,(5,600))
    screen.blit(text4, (505,600))

def DeathA1():
    text_box()
    text = myfont4.render('Our proud hero, helpless and terrified, lies uselessly on his seat,', False, (White), (0, 0, 0))
    text2 = myfont4.render('accepting his doomed fate like a pathetic lump.', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))

def DeathA2():
    text_box()
    text = myfont4.render('The explosive charge detonates prematurely. Its blast ignites the', False, (White), (0, 0, 0))
    text2 = myfont4.render('cabin into an inferno, pulverising our hero instantly.', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))

def end1A():
    crash = (pygame.transform.scale(get_image('EndA.jpg'), (1000, 700)))
    screen.blit((crash), (0, 0))
    text = myfont4.render('[Death A]', False, (White), (0, 0, 0))
    text2 = myfont4.render('Thank You For Playing', False, (White), (0, 0, 0))
    screen.blit(text,(5,5))
    screen.blit(text2,(500,650))

def sidedoor():
    sidedoor = (pygame.transform.scale(get_image('sidedoor.jpg'), (1000, 700)))
    screen.blit((sidedoor), (0, 0))
#Labeled based on how we labeled story in gdoc   
def textA3a():
    text_box()
    text = myfont4.render('You turn the handle on the cabin door. It smoothly slides into', False, (White), (0, 0, 0))
    text2 = myfont4.render('position', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    
def textA3b():
    text_box()
    text = myfont4.render('You give the door a gentle shove. You push a little harder. You', False, (White), (0, 0, 0))
    text2 = myfont4.render('steady your feet and push with all your might. The door doesn’t', False, (White), (0, 0, 0))
    text3 = myfont4.render('budge.', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))
    screen.blit(text3,(5, 620))
    
def textA3c():
    text_box()
    text = myfont4.render('Now what?', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))

def textA2a():
    text_box()
    text = myfont4.render('You stand at the tail end and spot the brown explosive charge', False, (White), (0, 0, 0))
    text2 = myfont4.render('on the side wall. You try to pry it off, but it appears to be', False, (White), (0, 0, 0))
    text3 = myfont4.render('stuck securely to the wall.', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))
    screen.blit(text3,(5, 620))
    
def onebutton3():
    text_box()
    text = myfont5.render('Investigate flight deck.', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))

def closed_door_text_1():
    text_box()
    text = myfont4.render('You stand at the doors to the cockpit, secured by a combination', False, (White), (0, 0, 0))
    text2 = myfont4.render('keypad, locked by a combination keypad lock.', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 580))
    screen.blit(text,(5,540))

def closed_door_text_2():
    text_box()
    text = myfont4.render('It appears our hero’s luck has, sadly, run out already, for his chances', False, (White), (0, 0, 0))
    text2 = myfont4.render('to guess the right 4-digit code would be 1 in 5040...', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))
    
def closed_door_text_3():
    text_box()
    text = myfont4.render('It would be nearly impossible for him to correctly guess', False, (White), (0, 0, 0))
    text2 = myfont4.render('the code was 0525!', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 580))
    screen.blit(text,(5,540))

def opendoor_button_text():
    text = myfont5.render('0525', False, (White), (0, 0, 0))
    text2 = myfont5.render('6969', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 640))
    screen.blit(text,(5,540))

def opendoor1():
    text_box()
    text = myfont4.render('By pure chance, you guess the right code!', False, (White), (0, 0, 0))
    text2 = myfont4.render('A once-in-a-lifetime miracle!', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 580))
    screen.blit(text,(5,540))

def opendoor2():
    opend = (pygame.transform.scale(get_image('opendoor.jpg'), (1000, 700)))
    screen.blit((opend), (0, 0))
    text_box()
    text = myfont4.render('You enter the cockpit, heartbeat quickening as you ', False, (White), (0, 0, 0))
    text2 = myfont4.render('gently open the door.', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 580))
    screen.blit(text,(5,540))

def opendoor3():
    opend = (pygame.transform.scale(get_image('cockpit.jpg'), (1000, 700)))
    screen.blit((opend), (0, 0))
    text_box()
    text = myfont4.render('But alas, the flight deck is deserted, any trace of the ', False, (White), (0, 0, 0))
    text2 = myfont4.render('pilots nowhere to be seen.', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 580))
    screen.blit(text,(5,540))

def death69_preview():
    text_box()
    text = myfont4.render('lmao nice', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def death69():
    end69 = (pygame.transform.scale(get_image('EndA.jpg'), (1000, 700)))
    screen.blit((end69), (0, 0))
    text = myfont4.render('[Death 69]', False, (White), (0, 0, 0))
    text2 = myfont4.render('Thank You For Playing', False, (White), (0, 0, 0))
    screen.blit(text,(5,5))
    screen.blit(text2,(500,650))
    
def choice3_text():
    text = myfont5.render('Take the controls', False, (White), (0, 0, 0))
    text2 = myfont5.render('Interact with headset', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 640))
    screen.blit(text,(5,540))

def take_controls_text():
    text_box()
    text = myfont4.render('You take the captain’s seat and grasp the controls.', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def take_controls_choice():
    text = myfont5.render('Ascend', False, (White), (0, 0, 0))
    text2 = myfont5.render('Desend', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 640))
    screen.blit(text,(5,540))

def death_B_text_A():
    text_box()
    text = myfont4.render('You push hard on the controls and descend.', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def death_B_text_B():
    text_box()
    text = myfont4.render('You catch a streak of grey outside the window, appearing', False, (White), (0, 0, 0))
    text2 = myfont4.render('closer and closer…', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 580))
    screen.blit(text,(5,540))

def death_B_text_C():
    text_box()
    text = myfont4.render('The airliner directly collides with the other aircraft', False, (White), (0, 0, 0))
    text2 = myfont4.render('that flew into your path. The sheer force of the', False, (White), (0, 0, 0))
    text3 = myfont4.render('collision kills you instantly.', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))
    screen.blit(text3,(5, 620))

def death_B():
    endB = (pygame.transform.scale(get_image('collision.jpg'), (1000, 700)))
    screen.blit((endB), (0, 0))
    text = myfont4.render('[Death B]', False, (White), (0, 0, 0))
    text2 = myfont4.render('Thank You For Playing', False, (White), (0, 0, 0))
    screen.blit(text,(5,5))
    screen.blit(text2,(500,650))

def headset1():
    text_box()
    text = myfont4.render('You take the captain’s seat, putting on the headset.', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def headset2():
    text_box()
    text = myfont4.render('Controller: “-Cape Verde Air 17, do you read me?', False, (White), (0, 0, 0))
    text2 = myfont4.render('You must descend immediately.”', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 580))
    screen.blit(text,(5,540))

def headset3():
    text_box()
    text = myfont4.render('You: “Hello can you help me?! I don’t know how I got here,', False, (White), (0, 0, 0))
    text2 = myfont4.render('but I’m the only one on the plane and-”', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 580))
    screen.blit(text,(5,540))

def headset4():
    text_box()
    text = myfont4.render('Controller: “We can talk about that and whatever later,', False, (White), (0, 0, 0))
    text2 = myfont4.render('I need you to take the controls now! Push down on the', False, (White), (0, 0, 0))
    text3 = myfont4.render('yoke in front of you and descend!”', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))
    screen.blit(text3,(5, 620))

def headset5():
    text_box()
    text = myfont4.render('At this moment, the aircraft’s automated Traffic', False, (White), (0, 0, 0))
    text2 = myfont4.render('Collision Avoidance System joltingly comes to life,', False, (White), (0, 0, 0))
    text3 = myfont4.render('display flashing and speakers blaring.”', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))
    screen.blit(text3,(5, 620))

def TCAS_Traffic():
    text_box()
    text = myfont4.render('TCAS: "Traffic."', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def TCAS_Climb():
    text_box()
    text = myfont4.render('TCAS: "Climb!"', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def TCAS_Choice_text():
    text = myfont5.render('Follow controller’s instructions. Descend immediately.', False, (White), (0, 0, 0))
    text2 = myfont5.render('Follow TCAS instructions. Climb immediately.', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 640))
    screen.blit(text,(5,540))

def skyrim_death():
    endB = (pygame.transform.scale(get_image('skyrim.jpg'), (1000, 700)))
    screen.blit((endB), (0, 0))
    endB2 = (pygame.transform.scale(get_image('Skyrim_text.png'), (1000, 700)))
    screen.blit((endB2), (0, 0))

def stepping_out_of():
    text_box()
    text = myfont4.render('You pull on the controls hard. You feel slightly weightless as', False, (White), (0, 0, 0))
    text2 = myfont4.render('the aircraft begins to climb rapidly. In the corner of your eye,', False, (White), (0, 0, 0))
    text3 = myfont4.render('you catch a streak of grey whiz past the bottom the airplane.', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))
    screen.blit(text3,(5, 620))

def near_miss():
    text_box()
    text = myfont4.render('You just had a lucky near miss with a mid-air collision.', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def hydraulic1():
    hydro = (pygame.transform.scale(get_image('cabin.jpg'), (1000, 700)))
    screen.blit((hydro), (0, 0))
    text_box()
    text = myfont4.render('Stepping outside the cockpit, you discover a piece of', False, (White), (0, 0, 0))
    text2 = myfont4.render('hydraulic equipment at your feet.', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 580))
    screen.blit(text,(5,540))

def Hydaraulic_Jack():
    text_box()
    text = myfont4.render('You’ve acquired [Hydraulic Jack].', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def conflict_clear():
    text_box()
    text = myfont4.render('TCAS: “Clear of conflict.”', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def controller1():
    text_box()
    text = myfont4.render('Controller: “You’re still here kid? Thank god.”', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def controller2():
    text_box()
    text = myfont4.render('Controller: “Listen. You’re going to fly out of my range soon.”', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def controller3():
    text_box()
    text = myfont4.render('Controller: “But it’s ok. All you have to do is turn to headinG---”', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def oops_out_of_range():
    text_box()
    text = myfont4.render('Oops. It appears you have flown out of range.', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def investigate_text():
    text = myfont5.render('Investigate tail section', False, (White), (0, 0, 0))
    text2 = myfont5.render('Investigate forward door', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 640))
    screen.blit(text,(5,540))

def walk_through_cabin():
    text_box()
    text = myfont4.render('You walk through the cabin towards the end of the airplane.', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def blocking_aisle():
    text_box()
    text = myfont4.render('You see something blocking your way in the aisle that wasn’t', False, (White), (0, 0, 0))
    text2 = myfont4.render('there before. Above, the overhead compartment is open.', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 580))
    screen.blit(text,(5,540))

def shaken_open():
    text_box()
    text = myfont4.render('You: "Must’ve been shaken open."', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def parachute():
    text_box()
    text = myfont4.render('You’ve acquired [Emergency Parachute].', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def choice6_button_text():
    text = myfont5.render('Investigate tail section', False, (White), (0, 0, 0))
    text2 = myfont5.render('Approach aft door. Attempt jump.', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 640))
    screen.blit(text,(5,540))

def explosive_charge_on_wall():
    text_box()
    text = myfont4.render('You stand at the tail end and spot the brown explosive charge', False, (White), (0, 0, 0))
    text2 = myfont4.render('on the side wall. You try to pry it off, but it appears to be stuck', False, (White), (0, 0, 0))
    text3 = myfont4.render('securely to the wall.', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))
    screen.blit(text3,(5, 620))

def now_what():
    text_box()
    text = myfont4.render('You: “Now what?”', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def choice7_button_text():
    text = myfont5.render('Approach forward door. Attempt jump.', False, (White), (0, 0, 0))
    text2 = myfont5.render('Approach aft door. Attempt jump.', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 640))
    screen.blit(text,(5,540))

def sidedoor2():
    sidedoor = (pygame.transform.scale(get_image('sidedoor.jpg'), (1000, 700)))
    screen.blit((sidedoor), (0, 0))

def blow_door_up():
    text_box()
    text = myfont4.render('You turn the release handle and prepare the hydraulic', False, (White), (0, 0, 0))
    text2 = myfont4.render('jack to blow the door off.', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 580))
    screen.blit(text,(5,540))

def smoothie():
    text_box()
    text = myfont4.render('The explosive decompression hurls you through the doorway in an', False, (White), (0, 0, 0))
    text2 = myfont4.render('instant. Without time to even react, you’re sucked into the', False, (White), (0, 0, 0))
    text3 = myfont4.render('enormous turbine engine, blending you into a human smoothie.', False, (White), (0, 0, 0))
    screen.blit(text,(5,540))
    screen.blit(text2,(5,580))
    screen.blit(text3,(5, 620))

def deathC_pic_and_text():
    endC = (pygame.transform.scale(get_image('smoothie.jpg'), (1000, 700)))
    screen.blit((endC), (0, 0))
    text = myfont4.render('[Death C]', False, (White), (0, 0, 0))
    text2 = myfont4.render('Thank You For Playing :D', False, (White), (0, 0, 0))
    screen.blit(text,(5,5))
    screen.blit(text2,(500,650))

def jump_sucess():
    text_box()
    text = myfont6.render('The explosive decompression hurls you through the doorway in an', False, (White), (0, 0, 0))
    text2 = myfont6.render('instant. Looking up, the lights of the aircraft soon become distant as', False, (White), (0, 0, 0))
    text3 = myfont6.render('you feel the rush of the air pound you. You hold onto the ripcord and', False, (White), (0, 0, 0))
    text4 = myfont6.render('wait until a safe altitude. You pull it away from you and feel the', False, (White), (0, 0, 0))
    text5 = myfont6.render('parachute deploy, looking down at the sea below you gently coming closer', False, (White), (0, 0, 0))
    screen.blit(text,(5,500))
    screen.blit(text2,(5,540))
    screen.blit(text3,(5,580))
    screen.blit(text4, (5,620))
    screen.blit(text5, (5, 660))

def coast_guard():
    text_box()
    text = myfont4.render('In the distance, you see a coast guard vessel cruising toward you,', False, (White), (0, 0, 0))
    text2 = myfont4.render('lights flashing and horns blaring.', False, (White), (0, 0, 0))
    screen.blit(text2,(5, 580))
    screen.blit(text,(5,540))

def saved():
    text_box()
    text = myfont4.render('You are saved!', False, (White), (0, 0, 0))
    screen.blit(text,(5, 540))

def good_end():
    win = (pygame.transform.scale(get_image('parachute.jpg'), (1000, 700)))
    screen.blit((win), (0, 0))
    text = myfont4.render('[You Win]', False, (White), (0, 0, 0))
    text2 = myfont4.render('Thank You For Playing :D. By: Griffin Kramer and Andrew Shao', False, (White), (0, 0, 0))
    screen.blit(text,(5,5))
    screen.blit(text2,(5,650))





pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode([screen_width,screen_height])
done = False
pygame.font.init()
myfont = pygame.font.SysFont('Helvetica', 30)
myfont2 = pygame.font.SysFont('Georgia', 40)
myfont3 = pygame.font.SysFont('Georgia', 35)
myfont4 = pygame.font.SysFont('Georgia', 33)
myfont5 = pygame.font.SysFont('Georgia', 20)
myfont6 = pygame.font.SysFont('Georgia', 30)

while not done:
        #clock.tick(10)
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:

                		done = True 
                screen.fill(White)
                #print(pygame.mouse.get_pressed())    
            
                start_game_image()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    story = 1

                if story == 1:
                        story_start()
                        if pygame.mouse.get_pressed() == (0, 0, 0):
                            off = 1

                if off == 1: 
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        cabin = 1

                if cabin == 1:
                    aircraft_cabin()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off1 = 1
                        
                if off1 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        ct1 = 1

                if ct1 == 1:
                    cabt1()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off2 = 1

                if off2 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        ct2 = 1

                if ct2 == 1:
                    cabt2()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off3 = 1
                    

                if off3 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        ct3 = 1

                if ct3 == 1:
                    cabt3()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off4 = 1
                    

                if off4 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        ct4 = 1


                if ct4 == 1:
                    cabt4()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off5 = 1


                if off5 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        box = 1

                if box == 1:
                    text_box()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off6 = 1


                if off6 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        ct5 = 1


                if ct5 == 1:
                    cabt5()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off7 = 1
                    

                if off7 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        ct6 = 1


                if ct6 == 1:
                    cabt6()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off8 = 1


                if off8 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        ct7 = 1

                if ct7 == 1:
                    cabt7()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off9 = 1
                    

                if off9 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        ct8 = 1

                if ct8 == 1:
                    cabt8()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off10 = 1



                if off10 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        ct9 = 1

                if ct9 == 1:
                    cabt9()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off11 = 1
                    

                if off11 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        ct10 = 1

                if ct10 == 1:
                    cabt10()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off12 = 1

                if off12 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        box2 = 1

                if box2 == 1:
                    text_box()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off13 = 1
                    

                if off13 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        ct11 = 1


                if ct11 == 1:
                    cabt11()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        off14 = 1

                if off14 == 1:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        choice1 = 1


                    
                if choice1 == 1:
                    screen.fill(White)
                    aircraft_cabin()
                    draw_buttons()
                    choice1_button_text()
                    if x == 0:
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            place = pygame.mouse.get_pos()
                            if place[0] >= 0 and place[0] <= 499 and place[1] >= 500 and place[1] <= 600:
                                    x = 1
                                    
                   
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            place = pygame.mouse.get_pos()
                            if place[0] >= 500 and place[0] <= 1000 and place[1] >= 500 and place[1] <= 600:
                                    x = 2

                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            place = pygame.mouse.get_pos()
                            if place[0] >= 0 and place[0] <= 500 and place[1] >= 600 and place[1] <= 700:
                                    x = 3            

                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            place = pygame.mouse.get_pos()
                            if place[0] >= 500 and place[0] <= 1000 and place[1] >= 600 and place[1] <= 700:
                                    x = 4




                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        c1off = 1
                    if c1off == 1:
                        #if hyd == 0:
                        if x == 4:
                            
                             DeathA1()
                             if pygame.mouse.get_pressed() == (0, 0, 0):
                                 offda1 = 1
                             if offda1 == 1:
                                 if pygame.mouse.get_pressed() == (1, 0, 0):
                                    da2 = 1
                             if da2 == 1:
                                     DeathA2()
                                     if pygame.mouse.get_pressed() == (0, 0, 0):
                                         offendA = 1 

                             if offendA == 1:
                                 if pygame.mouse.get_pressed() == (1, 0, 0):
                                     endA = 1

                             if endA == 1:
                                 end1A()
                                 

                        if x == 3:
                             '''
                             if pygame.mouse.get_pressed() == (0, 0, 0):
                                 offa3a = 1

                             if offa3a == 1:
                                 if pygame.mouse.get_pressed() == (1, 0, 0):
                                    a3a = 1
                             if a3a == 1:
                             '''
                             sidedoor()
                             textA3a()
                             if pygame.mouse.get_pressed() == (0, 0, 0):
                                 offa3b = 1 

                             if offa3b == 1:
                                 if pygame.mouse.get_pressed() == (1, 0, 0):
                                    a3b = 1
                             if a3b == 1:
                                     textA3b()
                                     if pygame.mouse.get_pressed() == (0, 0, 0):
                                         offa3c = 1

                             if offa3c == 1:
                                  if pygame.mouse.get_pressed() == (1, 0, 0):
                                     a3c = 1
                             if a3c == 1:
                                     textA3c()
                                     if pygame.mouse.get_pressed() == (0, 0, 0):
                                         offa3d = 1
                             if offa3d == 1:
                                  if pygame.mouse.get_pressed() == (1, 0, 0):
                                     a3d = 1

                             if a3d == 1:
                                  onebutton()
                                  onebutton3()
                                  if pygame.mouse.get_pressed() == (0, 0, 0):
                                      offa3e = 1
                                         
                             if offa3e == 1:
                                  if pygame.mouse.get_pressed() == (1, 0, 0):
                                      place = pygame.mouse.get_pos()
                                      if place[0] >= 0 and place[0] <= 1000 and place[1] >= 500 and place[1] <= 700:
                                          x = 1     
                            


                                    
                        if x == 2:
                             textA2a()
                             if pygame.mouse.get_pressed() == (0, 0, 0):
                                 offa2a = 1 

                             if offa2a == 1:
                                 if pygame.mouse.get_pressed() == (1, 0, 0):
                                    a2b = 1
                             if a2b == 1:
                                     textA3c()
                                     if pygame.mouse.get_pressed() == (0, 0, 0):
                                         offa2b = 1

                             if offa2b == 1:
                                  if pygame.mouse.get_pressed() == (1, 0, 0):
                                     a2a = 1

                             if a2a == 1:
                                  onebutton()
                                  onebutton3()
                                  if pygame.mouse.get_pressed() == (0, 0, 0):
                                      offa2c = 1
                                         
                             if offa2c == 1:
                                  if pygame.mouse.get_pressed() == (1, 0, 0):
                                      place = pygame.mouse.get_pos()
                                      if place[0] >= 0 and place[0] <= 1000 and place[1] >= 500 and place[1] <= 700:
                                          x = 1   


                        if x == 1:
                             button1()
                             closed_door_text_1()
                             if pygame.mouse.get_pressed() == (0, 0, 0):
                                 cdo1 = 1 

                             if cdo1 == 1:
                                 if pygame.mouse.get_pressed() == (1, 0, 0):
                                    cd1 = 1
                             if cd1 == 1:
                                     closed_door_text_2()
                                     if pygame.mouse.get_pressed() == (0, 0, 0):
                                         cdo2 = 1
                             if cdo2 == 1:
                                 if pygame.mouse.get_pressed() == (1, 0, 0):
                                    cd3 = 1
                             if cd3 == 1:
                                     closed_door_text_3()
                                     if pygame.mouse.get_pressed() == (0, 0, 0):
                                         cdo4 = 1

                             if cdo4 == 1:
                                 if pygame.mouse.get_pressed() == (1, 0, 0):
                                    cdo3 = 1

                             if cdo3 == 1:
                                 if pygame.mouse.get_pressed() == (0, 0, 0):
                                    choice2 = 1
                                    
                             if choice2 == 1:
                                draw_2buttons()
                                opendoor_button_text()
                                if z == 0:
                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                        place2 = pygame.mouse.get_pos()
                                        if place2[0] >= 0 and place2[0] <= 1000 and place2[1] >= 500 and place2[1] <= 600:
                                                z = 1
                                            
                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                        place2 = pygame.mouse.get_pos()
                                        if place2[0] >= 0 and place2[0] <= 1000 and place2[1] >= 600 and place2[1] <= 700:
                                                z = 2
                                if z == 2:
                                    death69_preview()
                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                        d69 = 1 

                                    if d69 == 1:
                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                            d70 = 1
                                    if d70 == 1:
                                        death69()

                                if z == 1:
                                    opendoor1()
                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                        od1 = 1 

                                    if od1 == 1:
                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                            ofod = 1
                                    if ofod == 1:
                                        opendoor2()
                                        if pygame.mouse.get_pressed() == (0, 0, 0):
                                            od2 = 1

                                    if od2 == 1:
                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                            ofodb = 1

                                    if ofodb == 1:
                                        opendoor3()
                                        if pygame.mouse.get_pressed() == (0, 0, 0):
                                            od3 = 1

                                    if od3 == 1:
                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                            ofodc = 1

                                    if ofodc == 1:
                                        if pygame.mouse.get_pressed() == (0, 0, 0):
                                            choice3 = 1
                                            
                                    if choice3 == 1:
                                        draw_2buttons()
                                        choice3_text()
                                        if y == 0:
                                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                                place3 = pygame.mouse.get_pos()
                                                if place3[0] >= 0 and place3[0] <= 1000 and place3[1] >= 500 and place3[1] <= 600:
                                                        y = 1
                                                    
                                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                                place3 = pygame.mouse.get_pos()
                                                if place3[0] >= 0 and place3[0] <= 1000 and place3[1] >= 600 and place3[1] <= 700:
                                                        y = 2

                                        if y == 1:
                                            take_controls_text()
                                            if pygame.mouse.get_pressed() == (0, 0, 0):
                                                ctrl = 1 

                                            if ctrl == 1:
                                                if pygame.mouse.get_pressed() == (1, 0, 0):
                                                    choice_take_controls = 1

                                            if choice_take_controls == 1:
                                                draw_2buttons()
                                                take_controls_choice()
                                                if con == 0:
                                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                                        place3 = pygame.mouse.get_pos()
                                                        if place3[0] >= 0 and place3[0] <= 1000 and place3[1] >= 500 and place3[1] <= 600:
                                                                con = 1
                                                            
                                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                                        place3 = pygame.mouse.get_pos()
                                                        if place3[0] >= 0 and place3[0] <= 1000 and place3[1] >= 600 and place3[1] <= 700:
                                                                con = 2
                                                if con == 2:
                                                    death_B_text_A()
                                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                                        deathB_A = 1

                                                    if deathB_A == 1:
                                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                                            deathB_offA = 1

                                                    if deathB_offA == 1:
                                                        death_B_text_B()
                                                        if pygame.mouse.get_pressed() == (0, 0, 0):
                                                            deathB_B = 1 

                                                    if deathB_B == 1:
                                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                                            deathB_offB = 1

                                                    if deathB_offB == 1:
                                                        death_B_text_C()
                                                        if pygame.mouse.get_pressed() == (0, 0, 0):
                                                            deathB_C = 1            

                                                    if deathB_C == 1:
                                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                                            deathB_offC = 1

                                                    if deathB_offC == 1:
                                                        death_B()
                                                
                                                if con == 1:
                                                    stepping_out_of()
                                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                                        near_miss_off = 1

                                                    if near_miss_off == 1:
                                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                                            near_miss_on = 1

                                                    if near_miss_on == 1:
                                                        near_miss()
                                                        if pygame.mouse.get_pressed() == (0, 0, 0):
                                                            hydraulic1_off = 1

                                                    if hydraulic1_off == 1:
                                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                                            hydraulic1_on = 1

                                                    if hydraulic1_on == 1:
                                                        hydraulic1()
                                                        if pygame.mouse.get_pressed() == (0, 0, 0):
                                                            Hydaraulic_Jack_not_on = 1

                                                    if Hydaraulic_Jack_not_on == 1:                                                                                 
                                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                                            Hydaraulic_Jack_on = 1

                                                    if Hydaraulic_Jack_on == 1:
                                                        Hydaraulic_Jack()
                                                        if pygame.mouse.get_pressed() == (0, 0, 0):
                                                            go_to_choice_5 = 1    

                                                    if go_to_choice_5 == 1:
                                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                                            hyd = 1

                                                   
                                                                                                 

                                        if y == 2:
                                            headset1()
                                            if pygame.mouse.get_pressed() == (0, 0, 0):
                                                hs1 = 1 

                                            if hs1 == 1:
                                                if pygame.mouse.get_pressed() == (1, 0, 0):
                                                    hs2 = 1
                                            if hs2 == 1:
                                                headset2()
                                                if pygame.mouse.get_pressed() == (0, 0, 0):
                                                    hs3 = 1

                                            if hs3 == 1:
                                                if pygame.mouse.get_pressed() == (1, 0, 0):
                                                    hs4 = 1

                                            if hs4 == 1:
                                                headset3()
                                                if pygame.mouse.get_pressed() == (0, 0, 0):
                                                    hs5 = 1

                                            if hs5 == 1:
                                                if pygame.mouse.get_pressed() == (1, 0, 0):
                                                    hs6 = 1

                                            if hs6 == 1:
                                                headset4()
                                                if pygame.mouse.get_pressed() == (0, 0, 0):
                                                    hs7 = 1

                                            if hs7 == 1:
                                                if pygame.mouse.get_pressed() == (1, 0, 0):
                                                    hs8 = 1

                                            if hs8 == 1:
                                                headset5()
                                                if pygame.mouse.get_pressed() == (0, 0, 0):
                                                    hs9 = 1

                                            if hs9 == 1:
                                                if pygame.mouse.get_pressed() == (1, 0, 0):
                                                    hs10 = 1

                                            if hs10 == 1:
                                                TCAS_Traffic()
                                                if pygame.mouse.get_pressed() == (0, 0, 0):
                                                    tcas_t = 1

                                            if tcas_t == 1:
                                                if pygame.mouse.get_pressed() == (1, 0, 0):
                                                    tcas_t2 = 1

                                            if tcas_t2 == 1:
                                                TCAS_Traffic()
                                                if pygame.mouse.get_pressed() == (0, 0, 0):
                                                    tcas_c = 1

                                            if tcas_c == 1:
                                                if pygame.mouse.get_pressed() == (1, 0, 0):
                                                    tcas_c2 = 1

                                            if tcas_c2 == 1:
                                                TCAS_Climb()
                                                if pygame.mouse.get_pressed() == (0, 0, 0):
                                                    tcas_c3 = 1

                                                if tcas_c3 == 1:
                                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                                        tcas_c4 = 1                                                

                                            if tcas_c4 == 1:
                                                if pygame.mouse.get_pressed() == (1, 0, 0):
                                                    tcas_c5 = 1

                                            if tcas_c2 == 1:
                                                TCAS_Climb()
                                                if pygame.mouse.get_pressed() == (0, 0, 0):
                                                    choice_ctrl = 1

                                                if choice_ctrl == 1:
                                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                                        choice_headset = 1





                                            if choice_headset == 1:
                                                draw_2buttons()
                                                TCAS_Choice_text()
                                                if tcas_choice == 0:
                                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                                        place3 = pygame.mouse.get_pos()
                                                        if place3[0] >= 0 and place3[0] <= 1000 and place3[1] >= 500 and place3[1] <= 600:
                                                                tcas_choice = 1
                                                            
                                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                                        place3 = pygame.mouse.get_pos()
                                                        if place3[0] >= 0 and place3[0] <= 1000 and place3[1] >= 600 and place3[1] <= 700:
                                                                tcas_choice = 2

                                                if tcas_choice == 1:
                                                    death_B_text_A()
                                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                                        D_S1 = 1

                                                    if D_S1 == 1:
                                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                                            D_S2 = 1

                                                    if D_S2 == 1:
                                                        death_B_text_B()
                                                        if pygame.mouse.get_pressed() == (0, 0, 0):
                                                            D_S3 = 1 

                                                    if D_S3 == 1:
                                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                                            D_S4 = 1

                                                    if D_S4 == 1:
                                                        screen.fill(Black)
                                                        if pygame.mouse.get_pressed() == (0, 0, 0):
                                                            D_S5 = 1            

                                                    if D_S5 == 1:
                                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                                            D_S6 = 1

                                                    if D_S6 == 1:
                                                        skyrim_death()

                                                if tcas_choice == 2:
                                                    stepping_out_of()
                                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                                        tcas1 = 1 

                                                if tcas1 == 1:
                                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                                        tcas2 = 1
                                                if tcas2 == 1:
                                                    controller1()
                                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                                        tcas3 = 1

                                                if tcas3 == 1:
                                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                                        tcas4 = 1

                                                if tcas4 == 1:
                                                    controller2()
                                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                                        tcas5 = 1

                                                if tcas5 == 1:
                                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                                        tcas6 = 1

                                                if tcas6 == 1:
                                                    controller3()
                                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                                        tcas7 = 1

                                                if tcas7 == 1:
                                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                                        tcas8 = 1

                                                if tcas8 == 1:
                                                    oops_out_of_range()
                                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                                        tcas9 = 1

                                                if tcas9 == 1:
                                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                                        tcas10 = 1

                                                if tcas10 == 1:
                                                    hydraulic1()
                                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                                        tcas11 = 1

                                                if tcas11 == 1:                                                                                 
                                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                                        tcas12 = 1

                                                if tcas12 == 1:
                                                    Hydaraulic_Jack()
                                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                                        tcas13 = 1    

                                                if tcas13 == 1:
                                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                                        hyd = 1
                                                            
                if hyd == 1:
                    draw_2buttons()
                    investigate_text()
                    if investigate == 0:
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            place5 = pygame.mouse.get_pos()
                            if place5[0] >= 0 and place5[0] <= 1000 and place5[1] >= 500 and place5[1] <= 600:
                                    investigate = 1
                                
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            place5 = pygame.mouse.get_pos()
                            if place5[0] >= 0 and place5[0] <= 1000 and place5[1] >= 600 and place5[1] <= 700:
                                    investigate = 2
                    
                    if investigate == 2:
                        death7B = 1

                    if investigate == 1:
                        walk_through_cabin()
                        if pygame.mouse.get_pressed() == (0, 0, 0):
                            walk_through_cabin_off = 1 

                        if walk_through_cabin_off == 1:
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                blocking_aisle_on = 1
                        if blocking_aisle_on == 1:
                            blocking_aisle()
                            if pygame.mouse.get_pressed() == (0, 0, 0):
                                blocking_aisle_off = 1

                        if blocking_aisle_off == 1:
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                shaken_open_on = 1

                        if shaken_open_on == 1:
                            shaken_open()
                            if pygame.mouse.get_pressed() == (0, 0, 0):
                                shaken_open_off = 1

                        if shaken_open_off == 1:
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                parachute_on = 1

                        if parachute_on == 1:
                            parachute()
                            if pygame.mouse.get_pressed() == (0, 0, 0):
                                parachute_off = 1

                        if parachute_off == 1:
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                go_to_choice_6 = 1

                        if go_to_choice_6 == 1:
                            if pygame.mouse.get_pressed() == (0, 0, 0):
                                choice6 = 1
                                
                        if choice6 == 1:
                            draw_2buttons()
                            choice6_button_text()
                            if emergency == 0:
                                if pygame.mouse.get_pressed() == (1, 0, 0):
                                    place6 = pygame.mouse.get_pos()
                                    if place6[0] >= 0 and place6[0] <= 1000 and place6[1] >= 500 and place6[1] <= 600:
                                            emergency = 1
                                        
                                if pygame.mouse.get_pressed() == (1, 0, 0):
                                    place6 = pygame.mouse.get_pos()
                                    if place6[0] >= 0 and place6[0] <= 1000 and place6[1] >= 600 and place6[1] <= 700:
                                            emergency = 2

                            if emergency == 2:
                                death7B = 2

                            if emergency == 1:
                                explosive_charge_on_wall()
                                if pygame.mouse.get_pressed() == (0, 0, 0):
                                    explosive_off = 1 

                                if explosive_off == 1:
                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                        now_what_on = 1
                                if now_what_on == 1:
                                    now_what()
                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                            now_what_off = 1

                                if now_what_off == 1:
                                    if pygame.mouse.get_pressed() == (1, 0, 0):
                                        go_to_choice_7 = 1

                                if go_to_choice_7 == 1:
                                    if pygame.mouse.get_pressed() == (0, 0, 0):
                                        choice7 = 1

                                if choice7 == 1:
                                    draw_2buttons()
                                    choice7_button_text()
                                    if jump == 0:
                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                            place7 = pygame.mouse.get_pos()
                                            if place7[0] >= 0 and place7[0] <= 1000 and place7[1] >= 500 and place7[1] <= 600:
                                                    jump = 1
                                                
                                        if pygame.mouse.get_pressed() == (1, 0, 0):
                                            place7 = pygame.mouse.get_pos()
                                            if place7[0] >= 0 and place7[0] <= 1000 and place7[1] >= 600 and place7[1] <= 700:
                                                    jump = 2 
                                    if jump == 1:
                                        death7B = 1

                                    if jump == 2:
                                        death7B = 2    

                
                if death7B == 1:
                    sidedoor2()
                    blow_door_up()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        deathC = 1 

                    if deathC == 1:
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            smoothie_on = 1

                    if smoothie_on == 1:
                        smoothie()
                        if pygame.mouse.get_pressed() == (0, 0, 0):
                            smoothie_off = 1            

                    if smoothie_off == 1:
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            deathC_control = 1
                    
                    if deathC_control == 1:
                        deathC_pic_and_text()


                if death7B == 2:
                    sidedoor2()
                    blow_door_up()
                    if pygame.mouse.get_pressed() == (0, 0, 0):
                        win_off = 1 

                    if win_off == 1:
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            sucess_on = 1

                    if sucess_on == 1:
                        jump_sucess()
                        if pygame.mouse.get_pressed() == (0, 0, 0):
                            sucess_off = 1            

                    if sucess_off == 1:
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            guard_on = 1

                    if guard_on == 1:
                        coast_guard()
                        if pygame.mouse.get_pressed() == (0, 0, 0):
                            guard_off = 1            

                    if guard_off == 1:
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            saved_on = 1

                    if saved_on == 1:
                        saved()
                        if pygame.mouse.get_pressed() == (0, 0, 0):
                            saved_off = 1            

                    if saved_off == 1:
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                            end_control = 1

                    if end_control == 1:        
                        good_end()


       

                pygame.display.update()
                #clock.tick(15)
pygame.display.update()
pygame.quit()
