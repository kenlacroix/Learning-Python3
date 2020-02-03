import random

#Declare guess, bet and balance now so we can use 'if' logic later on them
guess = str()
bet = int()
print("")
balance = int(input("How much are you bringing to the table? $"))

#Write your game of chance functions here

def coin_flip(guess, bet):
    print("_____________________________________")
    print(".......Game 1: flip-a-coin...........")
    print("-------------------------------------")

    print("")
    bet = int(input("How much are you betting?               $"))

    #Intake the bet and the guess and make sure balance < bet
    if balance < bet:
        print("")
        print("You should'nt bet more than your current balance")
        print("")
        return 0
    else:
        guess = str(input("Choose Heads or Tails:                  "))
        print("")

        flip = random.randint(1,2)

        #Evaluate the results of the flip
        if flip == 1:
            print ("Flip Results:         Tails")
        elif flip == 2:
            print("Flip Results:         Heads")
        else:
            print("Something went wrong, please try again")
            return

        #Compare the flip results against the guess, retrun the bet (+ or -)
        if (flip == 1 and guess == "Tails") or (flip == 2 and guess == "Heads"):
            print("")
            print("----------Winner, Winner!!!----------")
            print("")
            print("Current Balance:      $" + str(balance+bet) + " dollars")
            print("")
            return bet
        else:
            print("")
            print("--------------Loser!-----------------")
            print("")
            print("Current Balance:      $" + str(balance-bet) + " dollars")
            print("")
            return -bet

#Call your game of chance functions here

balance += coin_flip(guess,bet)
