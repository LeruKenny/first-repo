import random

opening = input('Do you want to play a game of rock ,paper ,scissors?(yes/no) ').lower()
if opening == "yes":
    True
elif opening == "no":
    False


while True:
    user_input = input("what is your guess? \ntype 'q' to quit - ").lower()
    mylist = ['rock', 'paper','scissors']
    computer_input = random.choice(mylist)
    if user_input == "q":
        break
    else:
        print(f'your guess is {user_input} and computer guess is {computer_input}')

    if user_input == computer_input:
        print('it is a tie')

    elif user_input == "rock":
        if computer_input == "scissors":
            print('you win')
        else:
            print('you lose')
    elif user_input == "scissors":
        if computer_input == "rock":
            print('you lose')
        else:
            print('you win')
    elif user_input == "paper":
        if computer_input == "scissors":
            print('you lose')
        else:
            print('you win')
    else:
        print('i dont know what you just typed')

while False:
    print('goodbye')
    break  
