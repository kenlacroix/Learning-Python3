#Write a function called unique_english_letters that takes the string word as
#a parameter. The function should return the total number of unique letters in
#the string. Uppercase and lowercase letters should be counted as different
#letters.
#
#We’ve given you a list of every uppercase and lower case letter in the English
#alphabet. It will be helpful to include that list in your function.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

def unique_english_letters(word):
    unique_letters = 0
    for letter in letters:
        if letter in word:
            unique_letters += 1
    return unique_letters

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
