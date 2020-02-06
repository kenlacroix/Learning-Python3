## More Frequent Item ##

#Create a function named more_frequent_item that has three parameters named lst,
#item1, and item2.

#Return either item1 or item2 depending on which item appears more often in lst.

#If the two items appear the same number of times, return item1.

#Write your function here

def more_frequent_item(lst, item1, item2):
  #Count the number of times item1 is in the list 'lst'. Expected value is 4.
  count1 = lst.count(item1)
  #Count the number of times item3 is in the list 'lst'. Expected value is 5.
  count2 = lst.count(item2)

  #Evaluate which is bigger. Return item1 if count1 and count2 are equal.
  if count1 >= count2:
    return item1
  else:
    return item2


#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
