import random, time

#Declare guess and bet now so we can use 'if' logic later on them
guess = str()
bet = int()
print("")

#Declare balance globally so we use it as a running total
balance = int(input("How much are you bringing to the table? $"))

#Write your game of chance functions here

def coin_flip(guess, bet):
    #Display game banner
    print("_____________________________________")
    print(".......Game 1: flip-a-coin...........")
    print("-------------------------------------")
    print("")

    #Explain rules
    print("Rules: You choose Heads or Tails, if correct, you win your bet")
    print("")

    #call the bet function to obtain the bet
    bet = bet()

    #Intake the bet and the guess and make sure balance < bet
    if bet <= 0:
        print("")
        print("Your bet must be a positive number")
        print("")
        return 0
    else:
        guess = str(input("Choose Heads or Tails:                  "))

        flip = random.randint(1,2)

        #Evaluate the results of the flip
        if flip == 1:
            print("Flip Results:                           Tails")
        elif flip == 2:
            print("Flip Results:                           Heads")
        else:
            print("Something went wrong, please try again")
            return

        #Compare the flip results against the guess, retrun the bet (+ or -)
        if (flip == 1 and guess == "Tails") or (flip == 2 and guess == "Heads"):
            winner()
            return bet
        else:
            loser()
            return -bet

def cho_han(guess,bet):

    print("Current Balance:                        $" + str(balance))
    print("_____________________________________")
    print("..........Game 2: Cho-Han............")
    print("-------------------------------------")
    print("")

    print("Rules: You choose Odd or Even then two dice are rolled and the value is summed. ")
    print("")

    #call the bet function to obtain the bet
    bet = bet()

    if bet <= 0:
        print("Your bet must be a positive number")
        return 0
    else:
        #Six sides to a die, so generate random number 1-6
        die_roll_1 = random.randint(1,6)
        die_roll_2 = random.randint(1,6)
        #Sum the two die rolls
        dice_roll = (die_roll_1 + die_roll_2)

        guess = str(input("Choose Even or Odd:                     "))

        print("The sum of the dice is:                 " + str(dice_roll))

        if dice_roll % 2 == 0 and guess == "Even":
            winner()
            return bet
        elif dice_roll % 2 == 1 and guess == "Even":
            Winner()
            return bet
        else:
            loser()
            return -bet
    return 0

def bet():
    bet = int(input("How much are you betting?               $"))
    return bet

def winner():
    print("")
    print("----------Winner, Winner!!!----------")
    print("")
    time.sleep(2)

def loser():
    print("")
    print("--------------Loser!-----------------")
    print("")
    time.sleep(2)

#Call your game of chance functions here
balance += coin_flip(guess,bet)
balance += cho_han(guess,bet)
