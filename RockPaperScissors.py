import random
import time

#displaying game rules
print("Winning rules of the game ROCK PAPER SCISSORS are:"
      "\nRock vs Paper -> Paper wins,"
      "\nRock vs Scissors -> Rock wins,"
      "\nPaper vs Scissors -> Scissors wins.")

while True:
    #input from user
    user_choice = int(input("Enter your choice by pressing:"
                   "\n1 - Rock"
                   "\n2 - Paper"
                   "\n3 - Scissors"
                   "\nChoice: "))

    #to get a valid input only
    if user_choice > 3 or user_choice < 1:
        user_choice = int(input("Please enter a valid choice."))

    #corresponding user's input to a choice value
    if user_choice == 1:
        print("You have chosen: Rock")
        user_choice_name = "Rock"
    elif user_choice == 2:
        print("You have chosen: Paper")
        user_choice_name = "Paper"
    else:
        print("You have chosen: Scissors")
        user_choice_name = "Scissors"

    #computer's input
    print(f"Now its Computer's turn to choose...")

    #to enhance the gaming experience (Choosing time)
    time.sleep(3)

    comp_choice = random.randint(1,3)

    #corresponding computer's choice to a choice value
    if comp_choice == 1:
        print("Computer has chosen: Rock")
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        print("Computer has chosen: Paper")
        comp_choice_name = "Paper"
    else:
        print("Computer has chosen: Scissors")
        comp_choice_name = "Scissors"

    #to enhance the gaming experience (processing time)
    time.sleep(5)

    #condition to check the possibility of a draw
    if user_choice == comp_choice:
        print(f"{user_choice_name} V/S {comp_choice_name}")
        print("\nIt's a DRAW.")

    #conditions for winning candidate
    if (user_choice == 1 and comp_choice == 2):
        print(f"{user_choice_name} V/S {comp_choice_name}")
        print(f"\n{comp_choice_name} wins."
          "\nHence, Computer wins")
    elif (user_choice == 2 and comp_choice == 1):
        print(f"{user_choice_name} V/S {comp_choice_name}")
        print(f"\n{user_choice_name} wins."
          "\nHence, User wins")

    if (user_choice == 1 and comp_choice == 3):
        print(f"{user_choice_name} V/S {comp_choice_name}")
        print(f"\n{user_choice_name} wins."
          "\nHence, User wins")
    elif (user_choice == 3 and comp_choice == 1):
        print(f"{user_choice_name} V/S {comp_choice_name}")
        print(f"\n{comp_choice_name} wins."
          "\nHence, Computer wins")

    if (user_choice == 3 and comp_choice == 2):
        print(f"{user_choice_name} V/S {comp_choice_name}")
        print(f"\n{user_choice_name} wins."
          "\nHence, User wins")
    elif (user_choice == 2 and comp_choice == 3):
        print(f"{user_choice_name} V/S {comp_choice_name}")
        print(f"\n{comp_choice_name} wins."
          "\nHence, Computer wins")

    #option to play again
    play_again = input(("Do you want to play again? (Y/N)")).upper()
    if play_again == "Y":
        continue
    else:
        break

print("Thanks for playing.")