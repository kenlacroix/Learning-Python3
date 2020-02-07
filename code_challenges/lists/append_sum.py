## Append Sum ##

#Write a function named append_sum that has one parameter named lst.

#he function should add the last two elements of lst together and append the
#result to lst. It should do this process three times and then return lst.

#For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2,
#3, 5, 8].

#Write your function here

def append_sum(lst):

    sum1 = lst[-1] + lst[-2]
    lst.append(sum1)
    print(lst)

    sum2 = lst[-1] + lst[-2]
    lst.append(sum2)
    print(lst)

    sum3 = lst[-1] + lst[-2]
    lst.append(sum3)
    print(lst)

    return lst



#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
