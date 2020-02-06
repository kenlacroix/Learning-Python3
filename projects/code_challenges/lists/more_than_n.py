## More than N ##

#Create a function named more_than_n that has three parameters named lst, item,
# and n.

#The function should return True if item appears in the list more than n times.
#The function should return False otherwise.

def more_than_n(lst, item, n):
  count = lst.count(item)
  #print(count)
  
  if count > n:
    print("The item " + str(item) + " is in the list more than " + str(n) + " times.")
    return True
  else:
    print("The item " + str(item) + " is not in the list more than " + str(n) + " times.")
    return False

#Expected value: True
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#Expected value: False
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 5))
