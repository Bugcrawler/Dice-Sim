import random
import time
Playing = True

# Mache eine schleife
# Mache eine eingabe

# While-loop
while Playing:
    while True:
        time.sleep(1)
        choice = input("Do you want to roll the dice?")

        if choice == "y":
            print("let's start")
            random_number = random.randint(1, 6)
            time.sleep(2)
            print("Rolling Dice...")
            time.sleep(1)
            print("...rolling...")
            time.sleep(1)
            print(random_number)
            time.sleep(2)
        elif choice == "n":
            print("Good Bye")
            quit()
        else:
            print("Stop this nonsens")


random_number = random.randint(1, 6)

print(random_number)

