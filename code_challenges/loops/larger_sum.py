#Create a function named larger_sum() that takes two lists of numbers as
#parameters named lst1 and lst2.
#
#The function should return the list whose elements sum to the greater number.
#If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
    #The variables that will hold the sums
    a = 0
    b = 0
    #Iterate through the first list
    for a1 in lst1:
        #Increment variable 'a' by the value of each item in the list 'lst1'
        a += a1
        #print(a)
    for b1 in lst2:
        b += b1
        #print(b)
    #Compare the two sums. If a if greater than or equal to b, return the first
    #list.
    if a >= b:
        return lst1
    #If a is not greater than or equal to b, return lst2
    else:
        return lst2


#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
