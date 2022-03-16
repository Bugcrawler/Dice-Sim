# imported modules
import random
import time

# Variables
Playing = True


# Dice-loop
while Playing:
    while True:
        time.sleep(1)
        Choice = input("Do you want to roll the dice? (Y/N)")

        # Case 1: Rolling the dice.
        if Choice == "Y":
            print("let's start")
            random_number = random.randint(1, 6)
            time.sleep(2)
            print("rolling...")
            time.sleep(1)
            print("...rolling...")
            time.sleep(1)
            print("And the number is...")
            time.sleep(1)
            print(random_number)
            time.sleep(2)

        # Case 2: Quitting the sim.
        elif Choice == "N":
            print("Good Bye")
            quit()
        else:
            print("Stop this nonsense.")
