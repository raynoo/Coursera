#http://www.codeskulptor.org/#user15_SCOowZxwF3_1.py

#Mini-project 4: Implementation of classic arcade game "Pong"
#to be run on www.codeskulptor.org

import simplegui
import random

#initialize globals
#canvas size
WIDTH = 700
HEIGHT = 400

#ball size, position, velocity
BALL_RADIUS = 15
BALL_POS = [WIDTH/2, HEIGHT/2]
BALL_VEL = [0, 0]

#paddle size, position, velocity
PADDLE_WIDTH = 8
PADDLE_HEIGHT = 80
HALF_PAD_WIDTH = PADDLE_WIDTH / 2
HALF_PAD_HEIGHT = PADDLE_HEIGHT / 2

#scores
SCORE_LEFT_POS = [WIDTH/2 - 65, HEIGHT/3]
SCORE_RIGHT_POS = [WIDTH/2 + 45, HEIGHT/3]

#flags
restart = True
time = 0.1

#colors
lightblue = "LightSteelBlue"
darkpink = "#B15B77"
teal = "DarkSlateGray"
lightgreen = "#33A2A2"

#spawns a ball by updating the ball's position and velocity vector
def throw_ball(right):
    global BALL_POS, BALL_VEL, time
    
    ball_init()
    time = 0.1
    
    velocity_x = random.randrange(10, 30)
    velocity_y = random.randrange(10, 30)
    
    if right:
        BALL_VEL[0] = velocity_x
    else:
        BALL_VEL[0] = -velocity_x
    
    BALL_VEL[1] = -velocity_y

def new_game():
    global time, restart, score_left, score_right, message, message_pos
    
    ball_init()  
    paddle_init()
    
    restart = True
    time = 0.1
    score_left = 0
    score_right = 0
    
    message = "Move a paddle to start!"
    message_pos = [WIDTH/2 - frame.get_canvas_textwidth(message, 20)/2, HEIGHT-80]

#reset the ball
def ball_init():
    global BALL_POS, BALL_VEL
    
    BALL_POS = [WIDTH/2, HEIGHT/2]
    BALL_VEL = [0, 0]

#reset the paddles
def paddle_init():
    global PADDLE_LEFT_POS, PADDLE_RIGHT_POS, PADDLE_VEL, PADDLE_LEFT_VEL, PADDLE_RIGHT_VEL
    
    PADDLE_LEFT_POS = [0, HEIGHT/2 - PADDLE_HEIGHT/2]
    PADDLE_RIGHT_POS = [WIDTH-PADDLE_WIDTH, HEIGHT/2 - PADDLE_HEIGHT/2]
    PADDLE_VEL = 40
    PADDLE_LEFT_VEL = 0
    PADDLE_RIGHT_VEL = 0

#ball's collision control
def update_ball():
    global PADDLE_LEFT_POS, PADDLE_RIGHT_POS, score_left, score_right, last_scored, time
    
    #update ball's position according to velocity
    BALL_POS[0] += BALL_VEL[0] * time
    BALL_POS[1] += BALL_VEL[1] * time

    #collide and reflect off of left side of gutter
    if(BALL_POS[0] <= PADDLE_WIDTH + BALL_RADIUS):
        #stop the game if ball hits outside the left paddle
        if(BALL_POS[1] < PADDLE_LEFT_POS[1] or BALL_POS[1] > PADDLE_LEFT_POS[1] + PADDLE_HEIGHT):
            score_right += 1
            last_scored = "right"
            throw_ball(True)
        else:
            BALL_VEL[0] = - BALL_VEL[0]
    
    #collide and reflect off of right side of gutter
    elif(BALL_POS[0] >= WIDTH - PADDLE_WIDTH - BALL_RADIUS):
        #stop the game if ball hits outside the right paddle
        if(BALL_POS[1] < PADDLE_RIGHT_POS[1] or BALL_POS[1] > PADDLE_RIGHT_POS[1] + PADDLE_HEIGHT):
            score_left += 1
            last_scored = "left"
            throw_ball(False)
        else:
            BALL_VEL[0] = - BALL_VEL[0]
    
    #collide and reflect off of top and bottom of canvas
    elif((BALL_POS[1] <= BALL_RADIUS) or (BALL_POS[1] >= HEIGHT - BALL_RADIUS)):
            BALL_VEL[1] = - BALL_VEL[1]


#update paddles' vertical position, keep them inside the screen
def update_paddles():
    global PADDLE_LEFT_POS, PADDLE_RIGHT_POS, PADDLE_LEFT_VEL, PADDLE_RIGHT_VEL
    
    #update position
    PADDLE_LEFT_POS[1] += PADDLE_LEFT_VEL
    PADDLE_RIGHT_POS[1] += PADDLE_RIGHT_VEL
    
    
    #reset position
    if(PADDLE_RIGHT_POS[1] < 0):
        PADDLE_RIGHT_POS[1] = 0
    if(PADDLE_LEFT_POS[1] < 0):
        PADDLE_LEFT_POS[1] = 0
    if(PADDLE_RIGHT_POS[1] + PADDLE_HEIGHT > HEIGHT):
        PADDLE_RIGHT_POS[1] = HEIGHT - PADDLE_HEIGHT
    if(PADDLE_LEFT_POS[1] + PADDLE_HEIGHT > HEIGHT):
        PADDLE_LEFT_POS[1] = HEIGHT - PADDLE_HEIGHT

#event handlers --

def draw(c):
    global PADDLE_LEFT_POS, PADDLE_RIGHT_POS
    global score_left, score_right
    
    update_ball()
    update_paddles()
    
    #draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, lightblue)
    c.draw_line([PADDLE_WIDTH, 0],[PADDLE_WIDTH, HEIGHT], 1, lightblue)
    c.draw_line([WIDTH - PADDLE_WIDTH, 0],[WIDTH - PADDLE_WIDTH, HEIGHT], 1, lightblue)
    
    #draw paddles
    c.draw_polygon([(PADDLE_LEFT_POS[0], PADDLE_LEFT_POS[1]), 
                    (PADDLE_WIDTH, PADDLE_LEFT_POS[1]), 
                    (PADDLE_WIDTH, PADDLE_LEFT_POS[1] + PADDLE_HEIGHT), 
                    (PADDLE_LEFT_POS[0], PADDLE_LEFT_POS[1] + PADDLE_HEIGHT)], 
                   2, lightblue, lightblue)
    c.draw_polygon([(PADDLE_RIGHT_POS[0], PADDLE_RIGHT_POS[1]), 
                    (WIDTH, PADDLE_RIGHT_POS[1]), 
                    (WIDTH, PADDLE_RIGHT_POS[1] + PADDLE_HEIGHT), 
                    (PADDLE_RIGHT_POS[0], PADDLE_RIGHT_POS[1] + PADDLE_HEIGHT)], 
                   2, lightblue, lightblue)
     
    #draw ball
    c.draw_circle(BALL_POS, BALL_RADIUS, 2, darkpink, darkpink)
            
    #draw scores
    c.draw_text(str(score_left), SCORE_LEFT_POS, 40, lightblue)
    c.draw_text(str(score_right), SCORE_RIGHT_POS, 40, lightblue)
    
    #draw begin message
    c.draw_text(message, message_pos, 20, lightgreen)

def keydown(key):
    global PADDLE_VEL, PADDLE_LEFT_POS, PADDLE_RIGHT_POS, restart, message
    global PADDLE_LEFT_VEL, PADDLE_RIGHT_VEL
    
    velocity = 6
    
    #move padleft up
    if(key == simplegui.KEY_MAP["w"]):
        PADDLE_LEFT_VEL -= velocity
        if restart:
            restart = False
            throw_ball(False)
    
    #move padleft down
    if(key == simplegui.KEY_MAP["s"]):
        PADDLE_LEFT_VEL += velocity
        if restart:
            restart = False
            throw_ball(False)
    
    #move padright up
    if(key == simplegui.KEY_MAP["up"]):
        PADDLE_RIGHT_VEL -= velocity
        if restart:
            restart = False
            throw_ball(True)
    
    #move padright down
    if(key == simplegui.KEY_MAP["down"]):
        PADDLE_RIGHT_VEL += velocity
        if restart:
            restart = False
            throw_ball(True)
    
    message = " "

def keyup(key):
    global PADDLE_LEFT_POS, PADDLE_RIGHT_POS, PADDLE_VEL
    global PADDLE_LEFT_VEL, PADDLE_RIGHT_VEL
    
    if(key == simplegui.KEY_MAP["w"]):
        PADDLE_LEFT_VEL = 0
    
    if(key == simplegui.KEY_MAP["s"]):
        PADDLE_LEFT_VEL = 0
    
    if(key == simplegui.KEY_MAP["up"]):
        PADDLE_RIGHT_VEL = 0
    
    if(key == simplegui.KEY_MAP["down"]):
        PADDLE_RIGHT_VEL = 0

def tick():
    global time
    time += 0.1

#create frame and register handlers
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_canvas_background(teal)

#draw restart button
frame.add_button("Start Over", new_game)

#help text
frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_label("Keys to use:")
frame.add_label("")
frame.add_label("w - left paddle up")
frame.add_label("s - left paddle down")
frame.add_label("up arrow   - right paddle up")
frame.add_label("down arrow - right paddle up")

timer = simplegui.create_timer(5000, tick)

#initialize game elements
new_game()

#start frame and timer
frame.start()
timer.start()