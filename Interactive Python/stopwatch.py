#Mini-Project 3: A simple game to hit a whole number in a Stopwatch
#to be run on www.codeskulptor.org

import simplegui

# define global variables
position_timer = [80, 130]
position_stats = [75, 30]
position_msg = [45, 230]
width = 250
height = 250
interval = 100
time_a = 0
time_bc = 0
time_d = 0
game_won = 0
game_total = 0
win_msg = "Hit a Whole Number"

# helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format_time():
    return str(time_a) + ":" + "%02d" % time_bc + "." + str(time_d)

def format_stats():
    return "Score: " + str(game_won) + "/" + str(game_total)

def hit_whole_number():
    if(time_d == 0):
        return True
    else:
        return False

# event handler for Start button
# starts timer
def start():
    global win_msg
    timer.start()
    win_msg = ""

# event handler for Stop button
# stops timer
def stop():
    global game_won, game_total, win_msg, position_msg
    
    if(timer.is_running()):
        if(hit_whole_number()):
            game_won += 1
            win_msg = "Good Job!"
            position_msg[0] = 80
        else:
            win_msg = "Try Again!"
            position_msg[0] = 80
            
        game_total += 1
    
    timer.stop()

# event handler for Reset button
# resets time variables
def reset():
    timer.stop()
    
    global time_a, time_bc, time_d, game_won
    global game_total, win_msg, position_msg
    time_a = 0
    time_bc = 0
    time_d = 0
    game_won = 0
    game_total = 0
    win_msg = "Hit a Whole Number"
    position_msg[0] = 45

# event handler for timer with 0.1 sec interval
# increment time variables at each interval
def tick():
    global time_a, time_bc, time_d

    if(time_bc == 59):
        time_bc = 0
        time_a += 1
    elif(time_d == 9):
        time_d = 0
        time_bc +=1
    else:
        time_d += 1

# handler to draw timer on canvas
def draw(canvas):
    canvas.draw_text(format_time(), position_timer, 36, "CornflowerBlue")
    canvas.draw_text(format_stats(), position_stats, 25, "Ivory")
    canvas.draw_text(win_msg, position_msg, 20, "PaleVioletRed")
    
# create frame
frame = simplegui.create_frame("Stopwatch", width, height)

# register event handlers for 3 buttons
text = frame.add_button("Start", start)
text = frame.add_button("Stop", stop)
text = frame.add_button("Reset", reset)

# register draw handler
frame.set_draw_handler(draw)

# create timer and register it's handler
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()
