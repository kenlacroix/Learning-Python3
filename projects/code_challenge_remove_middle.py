#Create a function named remove_middle which has three parameters named lst, start, and end.

#The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.

#For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

#Write your function here

def remove_middle(lst, start, end):
  #list[start:end]
  #Get the list 'lst' that starts at 0 and ends at the passed paameter of 1. The value would be '4'.
  first_half = lst[:start]
  print('First half: '+ str(first_half))

  #Increment the passed paramter (end). So that we start next index.
  end = end + 1
  last_half = lst[end:]
  print('Second Half: ' + str(last_half))

  #Combine the lists and return it.
  new_list = first_half + last_half
  return new_list

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
