import random
import sys
from time import sleep
ace = "Ace" 
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
ten = 10
jack = 10
queen = 10
king = 10
hand = 0 
dealers_hand = 0
valid_hand = True

deck = [ace, one, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king]

def draw():
    global hand
    draw = random.choice(deck)
    aoran = "a"
    if draw == ace:
        aoran = "an"
    print("You drew " + aoran + ": " + str(draw))
    
    if draw == ace:
        if hand + 11 > 21:
            hand += 1
        else:
            x = int(input("ACE! Input 1 or 11: "))
            if x > 1:
                hand += 11
            else: hand += 1
        
    else: hand += draw
    sleep(0.2)
    print ("Your hand equals: " + str(hand))
    sleep(0.2)

def turn():
    global valid_hand
    if hand == 0:
        sleep(0.5)
        draw()
        sleep(0.5)
        draw()
    turn = str(input("Stick or Twist? "))
    if turn.lower() == "twist":
        draw()
    elif turn.lower() == "stick":
        dealers_turn()
    
    if hand > 21:
        valid_hand = False
        sleep(0.2)
        print("Bust!")

def dealers_turn():
    global dealers_hand
    global valid_hand
    draw = random.choice(deck)
    aoran = "a"
    if draw == ace:
        aoran = "an"
    print("The Dealer drew " + aoran + ": " + str(draw))
    sleep(1)
    if draw == ace:
        if dealers_hand + 11 > 21:
            dealers_hand += 1
            if dealers_hand > 16:
                dealer_vs_player()
            else:
                dealers_turn()
        else:
            dealers_hand += 11
            if dealers_hand > 16:
                dealer_vs_player()
            else:
                dealers_turn()
            
    elif draw + dealers_hand > 21:
        dealers_hand += draw
        print("Dealers hand is " + str(dealers_hand))
        sleep(1)
        print("You Win!")
        valid_hand = False
    elif dealers_hand + draw > 16:
        dealers_hand += draw
        dealer_vs_player()
    else:
         dealers_hand += draw
         dealers_turn()



def dealer_vs_player():
    global hand
    global dealers_hand
    global valid_hand
    if hand > dealers_hand:
        print("Dealers hand is " + str(dealers_hand) + " Your hand is " + str(hand))
        sleep(1)
        print("You Win!")
        valid_hand = False
    elif dealers_hand > hand:
        print("Dealers hand is " + str(dealers_hand) + " Your hand is " + str(hand))
        sleep(1)
        print("You Lose!")
        valid_hand = False
    else:
        print("Dealers hand is " + str(dealers_hand) + " Your hand is " + str(hand))
        sleep(1)
        print("Draw!")
        valid_hand = False

def play_again():
    global valid_hand
    global dealers_hand
    global hand
    
    again = str(input("Do you want to play again? "))
    if again.lower() == "yes":
        valid_hand = True
        hand = 0
        dealers_hand = 0
    else:
        sys.exit()
   
    
    
while valid_hand == True:
    turn()
    while valid_hand == False:
       play_again()
            