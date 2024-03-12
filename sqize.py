print("Welcome to computer quize!!\n")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("------------------------------------\n")
print("okay! Let's play! :)")

count = 0
answer = input("\n1) What does CPU stands for? ")
if answer.lower() == "central processing unit" :
    print("Correct!")
    count+=1
else:
    print("Sorry Incorrect!")

answer = input("\n2) What does ROM stands for? ")
if answer.lower() == "read only memory" :
    print("Correct!")
    count+=1
else:
    print("Sorry Incorrect!")

answer = input("\n3) What does GPU stands for? ").lower()
if answer == "graphics processing unit" :
    print("Correct!")
    count+=1
else:
    print("Sorry Incorrect!")

answer = input("\n4) What does RAM stands for? ")
if answer.lower() == "random access memory" :
    print("Correct!")
    count+=1
else:
    print("Sorry Incorrect!")

answer = input("\n5) What does PSU stands for? ")
if answer.lower() == "power supply" :
    print("\nCorrect!")
    count+=1
else:
    print("\nSorry Incorrect!")

print("\n------------------------------------\n")
print(f"{count}/5")
print(f"You got {count} questions correct out of 5")
print("\n------------------------------------")


# print("\n Do you want to check answers? ")
# print("\n Question number: (press that number): \t 1)\t 2)\t 3)\t 4)\t 5)\t All\t To Quit : press 'q'")

# choice = input().lower()
# while(choice):
#     if choice!='q':
         
#         match choice:

#                 case "1": print("Central Processing Unit") 
#                 case "2": print("Read Only Memory")
#                 case "3": print("Graphics Processing Unit")
#                 case "4": print("Random Access Memory")
#                 case "5": print("Power Supply")
#                 case "all" :
#                             print("Central Processing Unit")
#                             print("Read Only Memory")
#                             print("Graphics Processing Unit")
#                             print("Random Access Memory")
#                             print("Power Supply")
#                 case "q": quit()
        
# print("Press Q to quit!")
# c = input().lower()
# if c=='q':
#      quit()





