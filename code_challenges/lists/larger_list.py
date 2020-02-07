## Larger List ##

#Write a function named larger_list that has two parameters named lst1 and lst2.

#The function should return the last element of the list that contains more
#elements. If both lists are the same size, then return the last element of
#lst1.

#Write your function here

def larger_list(lst1, lst2):
  lst1_len = len(lst1)
  lst2_len = len(lst2)

  if lst1_len > lst2_len:
    lst1 = lst1[-1]
    return lst1
  elif lst2_len > lst1_len:
    lst2 = lst2[-1]
    return lst2
  else:
    lst1 = lst1[-1]
    return lst1



#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))