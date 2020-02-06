## Creating and Appending Lists ##

#Create a new list 'last_semester_gradebook' and populate it.
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), \
("architecture", 65)]

#Create a new list 'subjects', populate and print it.
subjects = ['physics', 'calculus', 'poetry', 'history']
print(list(subjects))
print('')

#Create a new list 'grades', populate and print it.
grades = [98, 97, 85, 88]
print(list(grades))
print('')

#Merging 'names' and 'dogs_names' into a new list 'names_and_dogs_names' using
#zip() function.
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
names_and_dogs_names = zip(names, dogs_names)
print(names_and_dogs_names)


#Append new data to both 'subjects' and 'grades'.
subjects.append('computer science')
grades.append(100)
#Create a new list 'gradebook' and zip() 'subjects' and 'grades' and print it.
gradebook = list(zip(subjects, grades))
print(list(gradebook))
print('')

#Append 'gradebook' list with new data at the end of the list and print it.
gradebook.append(('visual arts', 93))
print(list(gradebook))
print('')

#zip() both 'gradebook' and 'last_semester_gradebook' into a new list
#'full_gradebook' and print it.
full_gradebook = list(zip(last_semester_gradebook, gradebook))
print(list(full_gradebook))
print('')

## Length of a list ##

#Generate a range that starts at 2, goes up to 20 (but not including) with an
#increment of 2. Assign value to a new list variable 'list1'. Expected value
#is 9.
list1 = range(2, 20, 2)

#Get and print the length of 'list1' and assign to new variable 'list1_len'.
list1_len = len(list1)
print(list1_len)

#Same thing as above but with an increment of 3. Expected value is '6'.
list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)

## Selecting List Elements I ##
#Create a new list 'employees' and populate it.
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']

#Create new variable and get index location 4 from 'employees' list. Expected
#result is 'Ryan'.
index4 = (employees[4])
print(index4)

#Print the length of the employees list. Expected result is '7'.
print(len(employees))

#Will cause an error because the list 'employess' has only 7 entries. Expected
#result is 'list index out of range'.
#print(employees[8])
#Select and index value that is in the range. Expected value is 'Dwight'.
print(employees[1])

## Selecting List Elements II ##

#Create and populate new list 'shopping_list'.
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']

#Print the length of the list. Expected value is '6'.
print(len(shopping_list))

#Get the last item in list 'shopping list', save a new variable 'last_element'
#and print it. Expected value is 'cerreal'.
last_element = shopping_list[-1]
print(last_element)

#Get elemement index 5 from 'shopping_list', save to new variable 'element5'
#and print it. Expected value is 'cereal'. Remember that numbers start at 0.
element5 = shopping_list[5]
print(element5)

## Slicing Lists ##
#Syntax: list[start:end]

#Create new list 'suitcase' and poplate it.
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

#Slice the list 'suitcase' by selecting elements 0 through 2. Does not select
#element 2, however. Print it. Expected return is ['shirt', 'shirt']
beginning = suitcase[0:2]
print(list(beginning))

#Samething as above except the first four elements are sliced. Expected
#return is ['shirt', 'shirt', 'pants', 'pants'].
beginning = suitcase[0:4]
print(list(beginning))

#Only the middle two items in 'suitcase'. Expected return is ['']
#Middle two elements in 'suitcase' are 2 and 3. We need a range of 2 through
#4 (but not including 4).
middle = suitcase[2:4]
print(middle)

##Slicing Lists II ##
#Syntax: list[:end]
#Syntax: list[-2:]
#Syntax: list[:-2]

#Define new list 'suitecase' and populate it.
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

#Define new list 'start' and populate it with the first three elements of
#'suitcase'. Print it. Expected returned value is ['shirt'. 'shirt', 'pants']
#Can omit the zero.
start = suitcase[:3]
print(start)

#The last 2 elements of suitcase. Expected return is ['pajamas', 'books']
end = suitcase[-2:]
print(end)

##Counting Elecments in a List
#Syntax: list.count('x')

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', \
'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', \
'Jake', 'Jake', 'Cassie', 'Laurie']

#Create new variable 'jakes_votes' and assign it the value of votes for 'Jake'.
#Expected return is 9.
jake_votes = votes.count('Jake')
print(jake_votes)

## Sorting Lists I ##

#Unsorted list. Prints: ['221 B Baker St.', '42 Wallaby Way',
#'12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave',
#'10 Downing St.']
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', \
'742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
print(addresses)

# Sorted list 'addresses'. Prints: ['221 B Baker St.', '42 Wallaby Way',
#'12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave',
#'10 Downing St.']
addresses.sort()
print(addresses)

#Unsorted list.
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
#You cannot do it this: sort(names)
#This will modify he list. Prints: ['Albus', 'Harry', 'Hermione', 'Ron',
# 'Sirius']
names.sort()
print(names)

#Unsorted list.
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']
print(cities)

#Returns 'none' because sort() does not return anything.
sorted_cities = cities.sort()
print(sorted_cities)

#Actually modify the list so its sorted. Expected return is:
#['London', 'Los Angeles', 'New York', 'Paris', 'Rome']
cities.sort()
print(cities)

## Sorting Lists II ##

#Unsorted List
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

#Sorts and creates a new list based on 'games'. Returns: ['Minecraft',
#'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']
games_sorted = sorted(games)
print(games_sorted)
#The original list, prints: ['Portal', 'Minecraft', 'Pacman', 'Tetris',
#'The Sims', 'Pokemon']
print(games)

## Lists Review ##

#A list
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', \
'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed',\
 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

#Get the length of the list 'inventory.' Returns: 19.
inventory_len = len(inventory)
print(inventory_len)

#Get the first index value of the list 'inventory'. Return: 'twin bed'.
first = inventory[1]
print(first)

#Get the last index value of the list 'inventory'. Returns: 'pillow'.
last = inventory[-1]
print(last)

#Get indexes 2 through 6 (but not including 6). Returns: ['headboard',
#'queen bed', 'king bed', 'dresser']
inventory_2_6 = inventory[2:6]
print (inventory_2_6)

#Get the first three indexes and save it to the variable 'first_3'. Returns:
#['twin bed', 'twin bed', 'headboard'].
first_3 = inventory[:3]
print(first_3)

#Get the number of 'twin bed' and save it to the variable 'twin_beds'.
#Returns 4.
twin_beds = inventory.count('twin bed')
print(twin_beds)

#Sort the list 'inventory' alphabetically. Returns: ['dresser', 'dresser',
#'headboard', 'king bed', 'king bed', 'king bed', 'nightstand', 'nightstand',
#'pillow', 'pillow', 'queen bed', 'sheets', 'sheets', 'table', 'table',
#'twin bed', 'twin bed', 'twin bed', 'twin bed']
inventory.sort()
print(inventory)
