from random import choice
from time import sleep

print("this program  plays rock, paper, scissor with you based on your choice")

#creates a dictionary to show the user all options and, a list to choose the numbers randomly
options = {0:"rock", 1:"paper", 2:"scissor"}
choosing = [0, 1, 2]
#this variable counts how many times the user won
counter_wins = 0
print("[0] rock\n[1] paper\n[2] scissor\n[3] quit")
while True:
    print("your score: {}".format(counter_wins))
    #here the computer makes the choice randomly
    computer_answer = choice(choosing)
    user_answer = int(input("type here your choice: "))
    if user_answer == 3: #it ends the game
        print("thank you for playing")
        break
    elif not user_answer in choosing and user_answer != 3: #in case the user types something that is not within the options
        print("type a number within the alternatives")
    sleep(0.5)
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PO")
    sleep(0.5)
    if computer_answer != user_answer: #it verifies the answers and it also tells the user if they won or lost
        if computer_answer == 0:
            if user_answer == 1:
                print("Computer: {}\nYou: {}\nYou Won!".format(options[computer_answer], options[user_answer]))
                counter_wins += 1
            else:
                print("Computer: {}\nYou: {}\nYou Lost.".format(options[computer_answer], options[user_answer]))
        elif computer_answer == 1:
            if user_answer == 2:
                print("Computer: {}\nYou: {}\nYou Won!".format(options[computer_answer], options[user_answer]))
                counter_wins += 1
            else:
                print("Computer: {}\nYou: {}\nYou Lost.".format(options[computer_answer], options[user_answer]))
        elif computer_answer == 2:
            if user_answer == 0:
                print("Computer: {}\nYou: {}\nYou Won!".format(options[computer_answer], options[user_answer]))
                counter_wins += 1
            else:
                print("Computer: {}\nYou: {}\nYou Lost.".format(options[computer_answer], options[user_answer]))
    else:
        print("Computer: {}\nYou: {}\nMatch.".format(options[computer_answer], options[user_answer]))
