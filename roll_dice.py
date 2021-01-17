import random

playing = True


while playing:
    roll = input("Press R to roll dice or E to exit: ")

    if roll.lower() == "r":
        print(random.randint(1,6))
        print ("Roll Again?")
        playing = True
        continue
    elif roll.lower() == "e":
        print("Thank you for playing!")
        break
    else:
        print("Incorrect Entry. Please press R or E")
        