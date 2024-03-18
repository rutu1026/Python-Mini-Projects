import random 

# random_number = random.randrange(11)    # range is 0 to 10. exclude the nuber 11
# r = random.randint(10)      # includes 10

top_of_range = input("Type a random number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter number greater than 0 next time!")
        quit()

else:
    print("Please enter a valid number next time!")
    quit()

random_number = random.randint(0,top_of_range)
# print(random_number)

# ---------------------

guesses = 0
while True:

    guesses+=1
    user_guess = input("\nMake a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess <= 0:
            print("Please enter number greater than 0 next time!")
            continue

    else:
        print("Please enter a valid number next time!")
        continue

    if user_guess == random_number:
        print("\nYou got correct!!")
        break

    elif user_guess < random_number:
        print("Your below than the number!")
        
    elif user_guess > random_number:
        print("You are above than the number!")
            
        # print("You got it wrong!")

print(f"You got it in {guesses} guessses!\n")