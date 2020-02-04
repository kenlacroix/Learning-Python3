import random, time

#Declare guess and bet now so we can use 'if' logic later on them
guess = str()
bet = int()
print("")

#Declare balance globally so we use it as a running total
balance = int(input("How much are you bringing to the table? $"))

#Write your game of chance functions here

#Game: Coin Flip. User calls Heads or Tails
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
    bet = int(get_bet())

    #Intake the bet and the guess and make sure bet < balance
    if bet <= 0:
        return 0
    else:
        if bet > balance:
            print("")
            print("You cannot bet more than your balance!!!")
            print("")
            return 0
        else:
            guess = str(input("Choose Heads or Tails:                  "))

            print("")
            print("The Coin is flipping.....")
            print("")
            time.sleep(2)

            #Generate either a '1' or a '2'
            flip = random.randint(1, 2)

            #Compare the flip results against the guess, retrun the bet (+ or -)
            if (flip == 1 and guess == "Heads") or (flip == 2 and guess == "Tails"):
                winner()
                return bet
            else:
                loser()
                return -bet

#Game: Cho-Han. Sum two dice rolls. User Chooses Odd or Even.
def cho_han(guess,bet):
    print("_____________________________________")
    print("..........Game 2: Cho-Han............")
    print("-------------------------------------")
    print("")

    print("Rules: You choose Odd or Even then two dice are rolled and the value is summed. ")
    print("")

    print("Current Balance:                        $" + str(balance))
    #call the bet function to obtain the bet
    bet = int(get_bet())


    if bet <= 0:
        return 0
    else:
        if bet > balance:
            print("")
            print("You cannot bet more than your balance!!!")
            print("")
            return 0
        else:
            #Six sides to a die, so generate random number 1-6
            die_roll_1 = random.randint(1,6)
            die_roll_2 = random.randint(1,6)
            #Sum the two die rolls
            dice_roll = (die_roll_1 + die_roll_2)

            guess = str(input("Choose Even or Odd:                     "))
            print("First die roll:                         " + str(die_roll_1))
            time.sleep(2)
            print("Second die roll:                        " + str(die_roll_2))
            time.sleep(2)
            print("The sum of the dice is:                 " + str(dice_roll))
            time.sleep(2)

            if dice_roll % 2 == 0 and guess == "Even":
                winner()
                return bet
            elif dice_roll % 2 == 1 and guess == "Odd":
                winner()
                return bet
            else:
                loser()
                return -bet

def two_card_draw(guess, bet):
    print("_____________________________________")
    print(".......Game 3: Two Card Draw.........")
    print("-------------------------------------")
    print("")

    print("Rules: Two cards are chosen, the higher one wins ")
    print("")

    print("Current Balance:                        $" + str(balance))
    bet = int(get_bet())

    your_card = random.randint(1,52)
    my_card = random.randint(1,52)

    if bet <= 0:
        return 0
    else:
        if bet > balance:
            print("")
            print("You cannot bet more than your balance!!!")
            print("")
            return 0
        else:
            if bet > balance:
                print("")
                print("You cannot bet more than your balance!!!")
                print("")
                return 0
            else:
                print("")
                print("Your card is:                           " + str(your_card))
                time.sleep(2)
                print("House card is:                          " + str(my_card))
                time.sleep(2)
                print("")

                #Compare cards, higher one wins
                if your_card > my_card:
                    winner()
                    return bet
                elif my_card > your_card:
                    loser()
                    return -bet
                elif my_card == your_card:
                    print("It was a tie!")
                    return 0
                else:
                    error()
                    return 0

#Game: Roulette Wheel. Instant lose if the ball lands on 0 or 00.
def roulette(guess, bet):
    print("_____________________________________")
    print("..........Game 4: Roulette...........")
    print("-------------------------------------")
    print("")

    print("""Rules: You guess a number between 0 and 36. If the ball
    lands on 0 or 00 of if you chose the wrong number, you lose. 37 is 00.""")
    print("")

    #Standard wheel has 36 slots, plus 00, which in this case is 37.
    landed_ball = random.randint(1, 37)

    print("Current Balance:                        $" + str(balance))
    bet = int(get_bet())

    if bet <= 0:
        error()
    else:
        if bet > balance:
            print("")
            print("You cannot bet more than your balance!!!")
            print("")
            return 0
        else:
            guess = int(input("Choose a number:                        "))
            if guess == 0 or guess == 37:
                error()
                return 0
            else:
                if guess > 37:
                    error()
                    return 0
                else:
                    print("")
                    print("The roulette wheel is spinning.....")
                    time.sleep(5)
                    if landed_ball == 37 or landed_ball == 0:
                        print("")
                        print("The ball landed on:                 0 or 00")
                        loser()
                        return -bet
                    else:
                        print("")
                        print("The ball landed on:                     " + str(landed_ball))
                        if guess == landed_ball:
                            winner()
                            return bet
                        else:
                            loser()
                            return -bet

def get_bet():
    bet = input("How much are you betting?               $")
    if bet.isnumeric() == True:
        return bet
    else:
        return 0

def error():
    print("")
    print("*** Error: Please check your input and try again!")
    print("")

def winner():
    print("")
    print("Result:                                 Winner!!!")
    print("")
    time.sleep(2)

def loser():
    print("")
    print("Result:                                 Loser :(")
    print("")
    time.sleep(2)

#Call your game of chance functions here
balance += coin_flip(guess,bet)
balance += cho_han(guess,bet)
balance += two_card_draw(guess,bet)
balance += roulette(guess,bet)
print("")
print("Your total winning/losses are:          $" + str(balance))
print("")
