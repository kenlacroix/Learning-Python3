#Create a function named odd_indices() that has one parameter named lst.
#
#The function should create a new empty list and add every element from lst
#that has an odd index. The function should then return this new list.
#
#For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list
#[3, 10, -2].


#Write your function here
#
#Define the funnction with one parameter, 'lst'
def odd_indices(lst):
    #Use a list comprehension return the index's value if it is odd.
    #For every item in 'lst', if it is odd, assign it to variable 'new_list'
    #List comprehension format:
    #variable = [expression for item in list if conditional]
    new_list = [lst[i] for i in range(len(lst)) if i % 2 == 1]
    #Return 'new_list'
    return(new_list)

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
