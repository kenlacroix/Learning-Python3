## Strings ##

#You’re a programmer working for Copeland’s Corporate Company. At
#this company, each employee’s user name is generated by taking the
#first five letters of their last name.
#
#A new employee, Rodrigo Villanueva, is starting today and you need
#to create his account. His first_name and last_name are stored as
#strings in script.py.
#
#Create a variable new_account by slicing the first five letters of
#his last_name.
first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
print(new_account)

#Temporary passwords for new employees are also generated from #their last
#names.
#
#Create a variable called temp_password by creating a slice out of #the third
#through sixth letters of his last_name.
temp_password = last_name[2:6]
print(temp_password)

#Copeland’s Corporate Company has realized that their policy of using the first
#five letters of an employee’s last name as a user name isn’t ideal when they
#have multiple employees with the same last name.
#
#Write a function called account_generator that takes two inputs, first_name and
#last_name and concatenates the first three letters of each and then returns the
#new account name.

## Concatenating Strings ##

#Write a function called account_generator that takes two inputs, first_name and
#last_name and concatenates the first three letters of each and then returns
#the new account name.

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
    #grab the first three letters of the first and last name
    threeFirst = first_name[:3]
    threeLast = last_name[:3]

    #concat the strings
    new_account = threeFirst + threeLast

#Create the new var and call the function
new_account = account_generator(first_name, last_name)

## String Slicing ##

#Copeland’s Corporate Company also wants to update how they generate temporary
#passwords for new employees.
#
#Write a function called password_generator that takes two inputs, first_name
#and last_name and then concatenate the last three letters of each and returns
#them as a string.

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
    #-3 starting at index 0 will give you the last three
    #In this example one doesnt really need to get the length, we can just start
    #at indice 0 and move backwards.
    lastThreeFirst = first_name[-3:]
    lastThreeLast = last_name[-3:]

    #return the concated strings
    return(lastThreeFirst + lastThreeLast)

#Test your function on the provided first_name and last_name and save it to the
#variable temp_password.
temp_password = password_generator(first_name, last_name)

## Negative Indices ##

#Use negative indices to find the the second to last character in company_motto.
#Save this to the variable second_to_last.
company_motto = "Copeland's Corporate Company helps you capably cope with the \
constant cacophony of daily life"

second_to_last = company_motto[-2]

#Use negative indices to create a slice of the last 4 characters in
#company_motto. Save this to the variable final_word.

#The last four letters starting at the negative 4th index and go to end.
final_word = company_motto[-4:]

## Strings are Immutable ##

## You cannot modify a string once it is created.

#The most recent hire at Copeland’s Corporate Company is a fellow named Rob
#Daily. Unfortunately, Human Resources seem to have made a bit of a typo and
#sent over the wrong first_name.

#Try changing the first character of first_name by running

first_name = "Bob"
last_name = "Daily"

#first_name[0] = "R" #TypeError: 'str' object does not support item assignment

#Oh right! Strings are immutable, so we can’t change an individual character.
#Okay, that’s no problem we can still fix this!
#
#Concatenate the string "R" with a slice of first_name that includes everything
#but the first character and save it to a new string fixed_first_name.

fixed_first_name = ("R" + first_name[1:])

## Escape Characters ##

#When Rob Daily (remember him? From the last exercise?) set up his account he
#set his password to be
#
#theycallme"crazy"91
#
#His password was causing some errors in the system because of the " marks.
#Rewrite his password using escape characters and save it to the variable
#password.

password = "theycallme\"crazy\"91"

## Iterating through Strings ##

#Let’s replicate a function you are already familiar with, len().
#
#Write a new function called get_length() that takes a string as an input and
#returns the number of characters in that string. Do this by iterating through
#the string, don’t cheat and use len()!

def get_length(string):
    count = 0
    #Iterate through the string
    for letter in string:
        #Increment the count each time the loop runs
        count += 1
    return count

## Strings and Conditionals (Part One) ##

#Write a function called letter_check that takes two inputs, word and letter.
#
#This function should return True if the word contains the letter and False
#if it does not.

def letter_check(word, letter):
    for i in word:
        if i == letter:
          return True
    else:
      return False

print(letter_check("strawberry", "o")) #False
print(letter_check("strawberry", "a")) #True

## Strings and Conditionals (Part Two) ##

#Write a function called contains that takes two arguments, big_string and
#little_string and returns True if big_string contains little_string.
#
#For example contains("watermelon", "melon") should return True and
#contains("watermelon", "berry") should return False.

def contains(big_string, little_string):
    return(little_string in big_string)

print(contains("watermelon", "melon")) #True
print(contains("watermelon", "berry")) #False

#Write a function called common_letters that takes two arguments, string_one
#and string_two and then returns a list with all of the letters they have in
#common.
#
#The letters in the returned list should be unique. For example,
#
#common_letters("banana", "cream") should return ['a'].

def common_letters(string_one, string_two):
    new_list = []
    for i in string_one:
        if i in string_two and i not in new_list:
          new_list.append(i)
    return new_list

print(common_letters("banana", "cream")) #returns ['a']
print(common_letters("Detroit", "Michigan")) #returns ['i']
print(common_letters("Lickitty", "Lemminy")) #returns ['L', 'i', 'y']

## Review ##

#1. Copeland’s Corporate Company has finalized what they want to their username
#and temporary password creation to be and have enlisted your help, once again,
#to build the function to generate them. In this exercise, you will create two
#functions, username_generator and password_generator.
#
#Let’s start with username_generator. Create a function called
#username_generator take two inputs, first_name and last_name and returns a
#username. The username should be a slice of the first three letters of their
#first name and the first four letters of their last name. If their first name
#is less than three letters or their last name is less than four letters it
#should use their entire names.
#
#For example, if the employee’s name is Abe Simpson the function should
#generate the username AbeSimp.

def username_generator(first_name, last_name):
    if len(first_name) <= 3 and len(last_name) <= 4:
        return(first_name + last_name)
    else:
        return(first_name[:3] + last_name[:4])


print(username_generator("Abe", "Simpson")) #returns: AbeSimp
print(username_generator("Mimiko", "Wantanabe")) #returns: MimWant
print(username_generator("Ricky", "Bobby")) #returns: RicBobb

#2. Great work! Now for the temporary password, they want the function to take
#the input user name and shift all of the letters by one to the right, so the
#last letter of the username ends up as the first letter and so forth. For
#example, if the username is AbeSimp, then the temporary password generated
#should be pAbeSim.
#
#Start by defining the function password_generator so that it takes one input,
#username and in it define an empty string named password.

def password_generator(first_name, last_name):
    for i in range(len(username)):
        password += username[i - 1]

#Inside password_generator create a for loop that iterates through the indices
#username by going from 0 to len(username).
#
#To shift the letters right, at each letter the for loop should add the previous
#letter to the string password.

def password_generator(username):
    password = ""
    for i in range(len(username)):
        password += username[i - 1]
    return password

print(password_generator(username_generator("Ricky", "Bobby")))