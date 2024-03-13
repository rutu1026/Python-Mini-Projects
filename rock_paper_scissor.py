import random

user_win = 0
computer_win = 0

options = ["rock" , "paper" , "scissor"]

while True:
    user = input("Choose Rock | Paper | Scissor or Q to quit:\n").lower()
    if user == 'q':
        # quit()
        break

    if user not in options:
        print("\n--> Enter valid choice\n")
        continue

    random_num = random.randint(0,2)
    # rock: 0, paper: 1, scissor: 2

    computer_pick = options[random_num]
    print("----------------------\n")
    print("Computer picked: ", computer_pick)

    if user == "rock" and computer_pick == "scissor":
        print("Yey! You Won!!")
        print("----------------------\n")
        user_win += 1

    elif user == "paper" and computer_pick == "rock":
        print("Yey! You Won!!")
        print("----------------------\n")
        user_win += 1

    elif user == "scissor" and computer_pick == "paper":
        print("Yey! You Won!!")
        print("----------------------\n")
        user_win += 1

    elif user == computer_pick:
        print("It's a tie!")
        print("----------------------\n")

    else:
        print("You lost!")
        print("\n----------------------\n")
        computer_win += 1
        
print("\n--------------------------------")
print("You won",user_win,"times")
print("Computer won",computer_win,"times")
print("Good bye!!\n")
