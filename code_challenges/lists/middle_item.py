## Middle Item ##

#Create a function called middle_element that has one parameter named lst.

#If there are an odd number of elements in lst, the function should return the
#middle element. If there are an even number of elements, the function should
#return the average of the middle two elements.


#Write your function here

def middle_element(lst):
  total_lst_len = len(lst)

  #Get the index of the middle element
  first_middle_num = int((len(lst)/2))
  #Get the index of the middle element - 1
  second_middle_num = int((len(lst)/2) - 1)

  #print(total_lst_len)
  #print(first_middle_num)
  #print(second_middle_num)

  #The list 'lst' length is even.
  if (total_lst_len % 2) == 0:

    #Get the value of the middle index
    first_middle_num = lst[first_middle_num]
    #Get the value of the middle index - 1
    second_middle_num = lst[second_middle_num]
    #Get the average of those two values by div by 2.
    avg_middle = ((first_middle_num + second_middle_num) / 2)
    #return the value
    return avg_middle
  #The list 'lst' length is odd.
  else:

    #Get the value of the middle index
    first_middle_num = lst[first_middle_num]
    #Return the value
    return first_middle_num



#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
print(middle_element([5, 2, -4, 4, 5]))
