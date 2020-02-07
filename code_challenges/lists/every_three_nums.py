## Every Three Numbers ##

#Create a function called every_three_nums that has one parameter named start.

#The function should return a list of every third number between start and 100
#(inclusive). For example, every_three_nums(91) should return the list [91, 94,
#7, 100]. If start is greater than 100, the function should return an empty
#list.

#Write your function here

def every_three_nums(start):
  #check to see if the start parameter is greather than 100.
  if start > 100:
    #Return an empty list 'lst'
    lst = []
    return lst
  else:
    #range(start, stop, increment)
    lst = list(range(start, 101, 3))
    return lst

#Uncomment the line below when your function is done
print(every_three_nums(91))
