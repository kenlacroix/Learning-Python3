#Create a function named double_index that has two parameters, a #list named lst
#and a single number as index.

#The function should return a new list where all elements are the #same as in
#lst except for the element at index, which should be #double the value of the
#element at index of lst.

#If index is not a valid index, the function should return the #original list.

#For example, the following code should return [1,2,6,4] because #the element
#at index 2 has been doubled:

#Write your function here

#define the function 'double_index'
def double_index(lst, index):
  #check if 'index' is greater than or equal to length of the list 'lst'.
  if index >= len(lst):
  #return the original list 'lst' since the index is out range.
    print('')
    print('The index is out range.')
    print('')
    return lst
  else:
    #Multiply the value of the supplied index by two and return the modified
    #list 'lst'.
    print("The index of " + str(index) + " has a value of: " + str(lst[index]))
    lst[index] = (lst[index] * 2)
    return lst

#Verify. Expected return: [3, 8, -20, 12]
print(double_index([3, 8, -10, 12], 2))
#Expected return: The index is out range. [3, 8, -10, 12]
print(double_index([3, 8, -10, 12], 4))
