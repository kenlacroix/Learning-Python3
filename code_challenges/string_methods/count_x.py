#Write a function named count_char_x that takes a string named word and a single
#character named x as parameters. The function should return the number of times
#x appears in word.

# Write your count_char_x function here:
def count_char_x(word, x):
    counter = 0
    for letters in word:
        if letters == x:
            counter += 1
    return counter

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
