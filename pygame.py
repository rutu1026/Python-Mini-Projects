import random

def roll():
    min_val = 1
    max_val = 6
  
    roll = random.randint(min_val,max_val)
    return roll

while True:

    max_players = input("Enter the players number(1-4): ")

    if max_players.isdigit():
        max_players = int(max_players)
        if 1<=max_players <= 4:
            break
        else:
            print("Invalid player numbers.\nPlayers must be 2 - 4")

    else:
        print("Invalid. Try again!")


max_score = 50
player_scores = [0 for _ in range(max_players)]

while max(player_scores) < max_score:

    for player_ind in range(max_players):
        print("\nPlayer number ", player_ind+1," turn has just started!\n")
        current_score = 0

        while True:

            should_roll = input("\nWould you want roll(y): ")
            if should_roll.lower() != 'y':
                break
            
            value = roll()
            if value == 1:
                print("You rolled one. Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled ",value)

            print("Your score is ",current_score)

        player_scores[player_ind] = current_score
        print("Your total score is ",player_scores[player_ind])

max_score = max(player_scores)
winning_ind = player_scores.index(max_score)
print("Player number ",winning_ind+1, "is the winner with score of ",max_score)