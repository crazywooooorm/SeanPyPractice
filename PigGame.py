#Pig Game Demo
#Sean

import random as r
def main():
    greet()
    game()
    bye()

def greet():
    print("Let's play this bullshit game.")

def bye():
    print("Game over, suckers.")

def rolldice():
    result = int(r.random() * 6 + 1)
    print("You got {}!".format(result))
    return result

def game():
    player_score = 0
    computer_score = 0
    while (player_score < 100 and computer_score <100):
        print("Now your score is {}!".format(player_score))
        player_score += playerMove()
        print("Now your score is {}!".format(player_score))
        if(player_score < 100):
            computer_score += computerMove()
            print("Now the computer's score is {}".format(computer_score))
    if(player_score > computer_score):
        print("You win, sucker!")
    else:
        print("You lose, sucker!")

def playerMove():
    choice = 'y'
    while(choice == 'y'):
        temp_score = 0
        temp = rolldice()
        if(temp == 1):
            print("You got {} in this round!".format(temp))
            temp = 0
            choice = 'n'
        else:
            print('you got {} in this round!'.format(temp))
            print('Do you want to roll again in this round?')
            choice = input('y/n ?')
        temp_score += temp
    print('Your round is over')
    print(" ")
    return temp_score

def computerMove():
    choice = 'y'
    while(choice == 'y'):
        temp_score = 0
        temp = rolldice()
        if(temp == 1):
            print('Computer got {} in this round'.format(temp))
            temp_score = 0
            choice = 'n'
        else:
            if(temp < 3.333):
                choice = 'y'
            else:
                choice = 'n'
                print('Computer got {} in this round'.format(temp))
        temp_score += temp
    print('Computer rouond is over')
    print('========================')
    print(' ')
    return temp_score


        
