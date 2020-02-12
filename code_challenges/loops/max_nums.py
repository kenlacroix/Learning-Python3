#Create a function named max_num() that takes a list of numbers named nums as
# parameter.

#The function should return the largest number in nums

#Write your function here

def max_num(nums):
    #Instead of iterating through a loop, just sort the list in ascendning
    #order.
    nums.sort()
    #Return the last value as it will be the largest since we sorted.
    return nums[-1]

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
