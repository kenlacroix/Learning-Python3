#Write a function named substring_between_letters that takes a string named
#word, a single character named start, and another character named end. This
#function should return the substring between the first occurrence of start
#and end in word. If start or end are not in word, the function should return
#word.

#For example, substring_between_letters("apple", "p", "e") should return "pl".


# Write your substring_between_letters function here:

def substring_between_letters(word, start, end):
    start_indice = word.find(start)
    end_indice = word.find(end)

    if start_indice != - 1 and end_indice != - 1:
        word = word[(start_indice + 1):end_indice]
        return word
    else:
        return word


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
