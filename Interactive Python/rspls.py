#Mini-project 1: A simple game of "Rock Paper Scissor Lizard Spock!" inspired by Sheldon Cooper

#<quote>
#it's very simple
#
#scissors cuts paper
#paper covers rock
#rock crushes lizard
#lizard poisons spock
#spock smashes scissors
#scissors decapitates lizard
#lizard eats paper
#paper disproves spock
#spock vaporizes rock
#
#and as it has always been
#
#rock crushes scissors
#</quote>


import random

def number_to_name(number):
    if(number == 0):
        return 'rock'
    elif(number == 1):
        return 'Spock'
    elif(number == 2):
        return 'paper'
    elif(number == 3):
        return 'lizard'
    elif(number == 4):
        return 'scissors'
    else:
        return 'error'

def name_to_number(name):
    if(name == 'rock'):
        return 0
    elif(name == 'Spock'):
        return 1
    elif(name == 'paper'):
        return 2
    elif(name == 'lizard'):
        return 3
    elif(name == 'scissors'):
        return 4
    else:
        return 'error'
    
def rpsls(name):
    player_number = name_to_number(name)
    comp_number = random.randrange(0,5)
    diff = (player_number - comp_number) % 5

#    print player_number, comp_number, diff
    
    if(diff == 1 or diff == 2):
        winner = "Player wins!"
    elif(diff == 3 or diff == 4):
        winner = "Computer wins!"
    else:
        winner = "Player and computer tie!"
    
    print "Player chooses " + name
    print "Computer chooses " + number_to_name(comp_number)
    print winner + "\n"

def test(p, c):
    player_number = name_to_number(p)
    comp_number = name_to_number(c)
    diff = (player_number - comp_number) % 5
    
    if(diff == 1 or diff == 2):
        winner = "Player wins!"
    elif(diff == 3 or diff == 4):
        winner = "Computer wins!"
    else:
        winner = "Player and computer tie!"
    
    print "Player chooses " + p
    print "Computer chooses " + c
    print winner + "\n"
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


#test("rock", "lizard")
#test("Spock", "scissors")
#test("paper", "rock")
#test("lizard", "rock")
#test("scissors", "scissors")