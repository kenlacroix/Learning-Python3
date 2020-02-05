# Author: Ken LaCroix
# Version: 1
# CodeAcademy "Games of Chance" Project
# https://www.kennethlacroix.me

#random is needed for RNG. time is needed to pause program execution.
import random, time

#Declare guess and bet now so we can use 'if' logic later on them
guess = str()
bet = int()

print("_____________________________________")
print("..........Games of Chance............")
print("            *Coin Flip")
print("             *Cho-Han")
print("          *Two Card Draw")
print("             *Roulette")
print("")
print("           By: Ken LaCroix")
print("    https://www.kennethlacroix.me")
print("-------------------------------------")
print("")

while True:
    try:
        balance = int(input("How much are you starting with?         $"))
        #Declare now so we can determine profit/loss later.
        init_balance = int(balance)
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        if balance <= 10:
            print("")
            print("*** Achievement Unlocked: From small beginings....")
            print("Difficulty: Common")
            print("")
            time.sleep(3)
        if balance >= 100 and balance <= 400:
            print("")
            print("*** Achievement Unlocked: Big Spenda")
            print("Difficulty: Common")
            print("")
            time.sleep(3)
        if balance >= 500 and balance < 1000:
            print("")
            print("*** Achievement Unlocked: Your know the money is fake....right?")
            print("Difficulty: Common")
            print("")
            time.sleep(3)
        if balance >= 1000:
            print("")
            print("*** Achievement Unlocked: Make'n it RRRAAAIIINNN!!!!!!")
            print("Difficulty: Common")
            print("")
            time.sleep(3)
        if balance <= 0:
            error()
        break

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
        error()
        return 0
    else:
        if bet > balance:
            print("")
            print("You cannot bet more than your balance!!!")
            print("")
            time.sleep(2)
            print("*** Achievement Unlocked: Doesn't play well with others.")
            print("Difficulty: Rare")
            print("")
            time.sleep(3)
            return 0
        else:
            while True:
                try:
                    guess = str(input("Choose Heads or Tails:                  "))
                except ValueError:
                    error()
                    continue
                else:
                    if guess == "Heads" or guess == "heads" or guess == "HEADS"\
                    or guess == "Tails" or guess == "tails" or guess == "TAILS":
                        print("")
                        print("The coin is in the air.....")
                        time.sleep(2)

                        #Generate either a '1' or a '2'
                        flip = random.randint(1, 2)

                        #Compare the flip results against the guess, retrun
                        #the bet (+ or -)
                        if (flip == 1 and guess == "Heads") or (flip == 1 and
                        guess == "heads") or (flip == 1 and guess == "HEADS") \
                        or (flip == 2 and guess == "Tails") or (flip == 2 and \
                        guess == "tails") or (flip == 2 and guess == "TAILS"):
                            winner()
                            print("*** Achievement Unlocked: A 50/50 chance.")
                            print("Difficulty: Common")
                            print("")
                            time.sleep(3)
                            return bet
                        else:
                            loser()
                            return -bet
                    else:
                        error()
                        return 0
                break


#Game: Cho-Han. Sum two dice rolls. User Chooses Odd or Even.
def cho_han(guess,bet):
    print("_____________________________________")
    print("..........Game 2: Cho-Han............")
    print("-------------------------------------")
    print("")

    print("Rules: You choose Odd or Even then two dice are rolled")
    print("and the value is summed. ")
    print("")

    print("Current Balance:                        $" + str(balance))
    #call the bet function to obtain the bet
    bet = int(get_bet())


    if bet <= 0:
        error()
        return 0
    else:
        if bet > balance:
            print("")
            print("You cannot bet more than your balance!!!")
            print("")
            time.sleep(2)
            return 0
        else:
            while True:
                try:
                    guess = str(input("Choose Even or Odd:                     "))
                except ValueError:
                    error()
                    continue
                else:
                    if guess == "Even" or guess == "even" or guess == "EVEN"\
                    or guess == "Odd" or guess == "odd" or guess == "ODD":
                        #Six sides to a die, so generate random number 1-6
                        die_roll_1 = random.randint(1,6)
                        die_roll_2 = random.randint(1,6)
                        #Sum the two die rolls
                        dice_roll = (die_roll_1 + die_roll_2)
                        print("First die roll:                         " + \
                        str(die_roll_1))
                        time.sleep(2)
                        print("Second die roll:                        " + \
                         str(die_roll_2))
                        time.sleep(2)

                        if (guess == "Even" and dice_roll % 2 == 0) or (guess \
                        == "EVEN" and dice_roll % 2 == 0) or (guess == "even" \
                        and dice_roll % 2 == 0):
                            winner()
                            print("*** Achievement Unlocked: Even Stephens.")
                            print("Difficulty: Common")
                            print("")
                            time.sleep(3)
                            return bet
                        elif (guess == "Odd" and dice_roll % 2 == 1) or (guess \
                        == "odd" and dice_roll % 2 == 1) or (guess == "ODD" and
                        dice_roll % 2 == 1):
                            winner()
                            return bet
                        else:
                            loser()
                            return -bet
                    else:
                        error()
                break

def two_card_draw(guess, bet):
    print("_____________________________________")
    print(".......Game 3: Two Card Draw.........")
    print("-------------------------------------")
    print("")

    print("Rules: Two cards are chosen, the higher one wins.")
    print("")

    print("Current Balance:                        $" + str(balance))
    bet = int(get_bet())

    your_card = random.randint(1,52)
    my_card = random.randint(1,52)

    if bet <= 0:
        error()
    else:
        if bet > balance:
            print("")
            print("You cannot bet more than your balance!!!")
            print("")
            time.sleep(2)
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
                print("*** Achievement Unlocked: One card to rule them all.")
                print("Difficulty: Common")
                print("")
                time.sleep(3)
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

    print("Rules: You guess a number between 0 and 36. If the")
    print("ball lands on 0 or 00 of if you chose the wrong")
    print("number, you lose. 00 is equal to 37. If you guess")
    print("correctly, there is a bet multiplier of 35.")
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
            time.sleep(2)
            return 0
        else:
            guess = int(input("Choose a number:                        "))
            #Insta-fail because the ball landed on 0 or 00 (37)
            if guess == 0 or guess == 37:
                #Since the user landed on 0 or 00, they insta-lose
                loser()
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
                        print("The ball landed on:                     " \
                        + str(landed_ball))
                        if guess == landed_ball:
                            winner()
                            #Adjust bet for multiplier, since the user won.
                            bet = (bet * 35)
                            print("*** Achievement Unlocked: Spinner Winner!!!")
                            print("Difficulty: Very Rare")
                            print("")
                            time.sleep(3)
                            return bet
                        else:
                            loser()
                            return -bet

#Check that the value is numeric, gets the input and returns the bet balance
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
    time.sleep(2)

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

#This function will increment/decrement 'achievement'. It will have some other
#logic that will unlock additional achievements like a winning streak of all
#four games, etc. Right now, it does nothing :(
def achievement(counter):
    print("")

#This 'if' structure will exit if the user runs out of money. If the balance
#stays positive, it will complete fully.
if balance > 0:
    balance += coin_flip(guess,bet)
    if balance > 0:
        balance += cho_han(guess,bet)
        if balance > 0:
            balance += two_card_draw(guess,bet)
            if balance > 0:
                balance += roulette(guess,bet)

if init_balance == balance:
    print("*** Achievement Unlocked: Atleast I broke even.")
    print("")
    time.sleep(3)
if balance > init_balance:
    print("*** Achievement Unlocked: Better put my winnings into a college-")
    print("savings plan")
    print("")
    time.sleep(3)

print("You started out with:                   $" + str(init_balance))
print("Your current balance is:                $" + str(balance))
print("You unlocked:                           x " + "achievements!")
print("")
