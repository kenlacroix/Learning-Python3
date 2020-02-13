## Strings ##

### Consider the following function. What would it print to the terminal? ##

def tell_me_about_icecream(favorite_icecream):
    response = "My favorite icecream is" + favorite_icecream + "."
    print(response)

tell_me_about_icecream("chocolate")

#### My favorite iscream ischocolate

### What code would select the letter “p” from the string good_fruit = "Raspberry"?

good_fruit[3]

### Which of the following expressions is False? ###

"s" in "watermelon" #correct answer

"cran" in "cranberrry" #True

"a" in "banana" #True

"cherry" in "cherry" #True

### What will the following code print to terminal? ###
def print_some_characters(word):
  for i in range(len(word)):
    if i % 2 == 0:
      print(word[i])

print_some_characters("watermelon")

####Prints the letters that have an even index
####w
####t
####r
####e
####o

### Given the string least_favorite_fruit = "cantaloupe", what piece of code
# would create a string that was equal to "lou"? ###

least_favorite_fruit[5:8]

### What character will be selected from the string cool_fruit = "watermelon"
# using the code cool_fruit[len(cool_fruit) - 2]? ###

'n' # incorrect
'o' # correct, gets the length, moves to the second to last index.
'This code will throw an IndexError' # incorrect
'i' # incorrect
