toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'anchovies']

prices = [2, 6, 1 ,3, 2, 7, 2]

#Get the length of the list 'toppings'.
num_pizzas = len(toppings)

#Print that length in a string.
print('We sell ' + str(num_pizzas) + " different kinds of pizzas!")

#Combine the 'prices' and 'toppings' lists using zip().
pizzas = list(zip(prices, toppings))
#Verify. Expected Value: [(2, 'pepperoni'), (6, 'pineapple'), (1, 'cheese'), (3, 'sausage'), (2, 'olives'), (7, 'anchovies'), (2, 'anchovies')]
#Verify. Expected value: 'We sell 7 different kinds of pizzas!'
print(pizzas)

#sort the list 'pizzas' lowest to highest.
pizzas.sort()
#Verify. Expected value: [(1, 'cheese'), (2, 'anchovies'), (2, 'olives'), (2, 'pepperoni'), (3, 'sausage'), (6, 'pineapple'), (7, 'anchovies')]
print(pizzas)

#Get the first element of the sorted list 'pizzas' and store in the variable 'cheapest_pizza'.
cheapest_pizza = pizzas[0]
#Verify. Expected value: (1, 'cheese')
print(cheapest_pizza)

#Get the last element in the last and store in variable 'priciest_pizza'.
priciest_pizza = pizzas[-1]
#Verify. Expected value: (7, 'anchovies')
print(priciest_pizza)

#Get the first three elements. '0' is ommited.
three_cheapest = pizzas[:3]
#Verify. Expected value: [(1, 'cheese'), (2, 'anchovies'), (2, 'olives')]
print(three_cheapest)

#Count the number of times '2' is in the 'prices' list.
num_two_dollar_slices = prices.count(2)
#Verify. Expected value: 3
print(num_two_dollar_slices)
