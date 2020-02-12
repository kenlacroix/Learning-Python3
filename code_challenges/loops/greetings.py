#Create a function named add_greetings() which takes a list of strings named
#names as a parameter.
#
#In the function, create an empty list that will contain each greeting. Add the
#string "Hello, " in front of each name in names and append the greeting to the
# list.
#
#Return the new list containing the greetings.

#Write your function here

#Define the function
def add_greetings(names):
    #create an empty list
    greeting = []
    #Iterate through the list
    for name in names:
        #Append 'Hello, ' and the name to the empty list.
        greeting.append("Hello, " + str(name))
    #Return the newly appended list
    return(greeting)

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
