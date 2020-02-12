#Create a function named exponents() that takes two lists as parameters
#named bases and powers. Return a new list containing every number in bases
#raised to every number in powers.

#For example, consider the following code.
#
#exponents([2, 3, 4], [1, 2, 3])
#
#the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first
#add two to the first. Then two to the second. Then two to the third, and
#so on.

#Write your function here

#Define the function with two parameters
def exponents(bases, powers):
    #Define an empty list
    new_list = []
    #The first loop that iterates through the bases
    for b in bases:
        #The second nested loop that iterates through the powers
        for p in powers:
            #Append to the 'new_list' the value of base ** power
            new_list.append(b ** p)
    #Return the new_list
    return(new_list)


#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
