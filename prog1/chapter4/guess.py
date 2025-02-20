# we need the random module to generate a random number
import random

if __name__=="__main__":
    # let's start by generating a random in [1,200] (1, 200 are inclusive)
    nb:int=random.randint(1,200)

    # since we don't give guess an intial value before reading it, we use
    # a seemingly infinie loop. This ons will halted when the user gives the right
    # answer
    while True:
        # read the user's guess
        guess:int=int(input("Your guess:"))
      
        if guess>nb: # the user guess is greather than the chosen number
            print("Your guess is greater")
        elif guess<nb: # the user guess is less than the chosen number
            print("Your guess is lower")
        else: # neither the first condition nor the second one is true. The only possibility is guess==nb, break the loop
            break
    print("Congratulations, your guess is correct:",guess)
