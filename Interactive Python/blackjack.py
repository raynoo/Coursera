#http://www.codeskulptor.org/#user15_q1X0xesxNiQyGQn_0.py

#Mini-project 6 - Implementation of a simple version of Blackjack
#to be run on www.codeskulptor.org

import simplegui
import random

#canvas
HEIGHT = 600
WIDTH = 600

# load card sprite - 950x392 - source: jfitz.com
CARD_SIZE = (73, 98)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

#positions
PLAYER_HAND_POS = [90, 430]
DEALER_HAND_POS = [90, 120]

PLAYER_LABEL_POS = [100, PLAYER_HAND_POS[1] + CARD_SIZE[1] + 45]
DEALER_LABEL_POS = [100, DEALER_HAND_POS[1] - 35]

OUTCOME_POS = [100, 370]
CHOICE_POS = [100, 290]

SCORE_POS = [WIDTH-110, PLAYER_LABEL_POS[1]]
DEALER_SCORE_POS = [WIDTH-110, DEALER_LABEL_POS[1]]

SCORE_LABEL_POS = [SCORE_POS[0]-60, SCORE_POS[1]]
DEALER_SCORE_LABEL_POS = [DEALER_SCORE_POS[0]-60, DEALER_SCORE_POS[1]]

#labels
player_label = "You"
dealer_label = "Dealer"
title = "Blackjack"
score_label = "Score: "

score = 0
dealer_score = 0
in_play = False
label_size_1 = 20
label_size_2 = 23
label_size_3 = 30

#colors
darkpink = "#A30052"
darkgreen = "#216343"
brown = "#5E3914"
darkbrown = "#38220C"
gray = "Gray"
gold = "#CCAC00"

class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print "Invalid card: ", self.suit, self.rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_SIZE[0] * (0.5 + RANKS.index(self.rank)), 
                    CARD_SIZE[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                          [pos[0] + CARD_SIZE[0] / 2, pos[1] + CARD_SIZE[1] / 2], 
                          CARD_SIZE)
        
class Hand:
    def __init__(self):
        self.card_list = []

    def __str__(self):
        s = "Hand contains "
        for c in self.card_list:
            s += str(c) + " "
        return s.rstrip()

    def add_card(self, card):
        self.card_list.append(card)

    def get_value(self):
        v = 0
        ace_present = False
        for c in self.card_list:
            v += VALUES[c.get_rank()]
            if c.get_rank() == 'A':
                ace_present = True
        
        if ace_present and v+10 <= 21:
            v += 10
        
        return v
        
    def busted(self):
        return self.get_value() > 21
    
    def draw(self, canvas, p):
        i=0
        for c in self.card_list:
            c.draw(canvas, [p[0] + i, p[1]])
            i += CARD_SIZE[0] + 5
        
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        self.shuffle()
        return self.deck.pop()

    def __str__(self):
        s = "Deck contains "
        for c in self.deck:
            s += str(c) + " "
        return s.rstrip()

def init():
    global outcome, in_play, player_hand, dealer_hand
    global deck, choice, score, dealer_label, dealer_score
    
    #initialize deck and hands
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    if in_play:
        #can't deal when already in a game
        outcome = "You lose for leaving a game!"
        dealer_score += 1
    else:
        outcome = ""
    
    choice = "Try a new Deal"
    in_play = False
    dealer_label = "Dealer"

def deal():
    global outcome, in_play, player_hand, dealer_hand
    global deck, dealer_score, player_score, choice
    
    init()
    
    #deal 2 cards
    for _ in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
    
    in_play = True
    choice = "Hit or Stand?"

def hit():
    global deck, player_hand, dealer_hand, outcome
    global in_play, choice, score, dealer_score
    
    if in_play:
        # if the hand is in play, hit the player
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
            
            # if busted, assign an message to outcome, update in_play and score
            if player_hand.busted():
                outcome = "You Lose! You have Busted!"
                choice = "New Deal?"
                in_play = False
                dealer_score += 1
       
def stand():
    global deck, dealer_hand, in_play, choice
    
    if in_play:
        #repeatedly hit dealer until his hand has value 17 or more
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())

        calculate_winner()

def calculate_winner():
    global player_hand, dealer_hand, outcome
    global in_play, score, choice, dealer_label, dealer_score
    
    if(player_hand.busted()):
        outcome = "You Lose! You have Busted!"
        dealer_score += 1
    
    elif(dealer_hand.busted()):
        outcome = "You Win! Dealer has Busted!"
        score += 1
    
    elif(dealer_hand.get_value() >= player_hand.get_value()):
        outcome = "You Lose!"
        dealer_score += 1
    
    else:
        outcome = "You Win!"
        score += 1
    
    in_play = False
    choice = "Try a new Deal"
    
    dealer_label += " [" + str(dealer_hand.get_value()) + "]"

def draw(canvas):
    global player_hand, dealer_hand, in_play
    
    player_hand.draw(canvas, PLAYER_HAND_POS)
    dealer_hand.draw(canvas, DEALER_HAND_POS)

    draw_labels(canvas)
    draw_frames(canvas, PLAYER_HAND_POS)
    draw_frames(canvas, DEALER_HAND_POS)
    
    if in_play:
        canvas.draw_image(card_back, [CARD_BACK_SIZE[0]/2, CARD_BACK_SIZE[1]/2], 
                          CARD_BACK_SIZE, 
                          [DEALER_HAND_POS[0] + CARD_BACK_SIZE[0] / 2, 
                           DEALER_HAND_POS[1] + CARD_BACK_SIZE[1] / 2], 
                          CARD_BACK_SIZE)

def draw_labels(canvas):
    canvas.draw_text(title, title_pos, label_size_3, gold)
    
    canvas.draw_text(player_label + " [" + str(player_hand.get_value()) + "]", 
                     PLAYER_LABEL_POS, label_size_1, darkbrown)
    canvas.draw_text(dealer_label, DEALER_LABEL_POS, label_size_1, darkbrown)
    
    canvas.draw_text(choice, CHOICE_POS, label_size_2, brown)
    canvas.draw_text(outcome, OUTCOME_POS, label_size_2, darkpink)
    
    canvas.draw_text(str(score), SCORE_POS, label_size_1, darkbrown)
    canvas.draw_text(score_label, SCORE_LABEL_POS, label_size_1, darkbrown)
    canvas.draw_text(str(dealer_score), DEALER_SCORE_POS, label_size_1, darkbrown)
    canvas.draw_text(score_label, DEALER_SCORE_LABEL_POS, label_size_1, darkbrown)
    
def draw_frames(canvas, card_pos):
    canvas.draw_line([80, card_pos[1] - 10], 
                     [WIDTH - 80, card_pos[1] - 10], 1, gray)
    canvas.draw_line([WIDTH - 80, card_pos[1] - 10], 
                     [WIDTH - 80, card_pos[1] + CARD_SIZE[1] + 10], 1, gray)
    canvas.draw_line([WIDTH - 80, card_pos[1] + CARD_SIZE[1] + 10], 
                     [80, card_pos[1] + CARD_SIZE[1] + 10], 1, gray)
    canvas.draw_line([80, card_pos[1] + CARD_SIZE[1] + 10], 
                     [80, card_pos[1] - 10], 1, gray)

#game board
frame = simplegui.create_frame("Blackjack", HEIGHT, WIDTH)
frame.set_canvas_background(darkgreen)

#game buttons
for _ in range(9):
    frame.add_label("")

frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

#initialize game varaibles
init()

#game title position
title_pos = [WIDTH/2 - frame.get_canvas_textwidth(title, label_size_3) / 2, 40]

frame.start()