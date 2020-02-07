## Loops ##

#for <temporary variable> in <list variable>:
#    <action>


#Define the list 'dog breeds' and populate it.
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

#Iterate through every item in the list and print each item.
for breed in dog_breeds:
    print(breed)

## Using Range in Loops ##

#Use the range function in a for loop to print out promise 5 times.

promise = "I will not chew gum in class"

for i in range(5):
    print(promise)

## Infinite Loop ##

#Normal 'for' loop
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for i in students_period_A:
    students_period_B.append(i)
    print(i)


#Infinite Loop because we are trying to append to the same list we are reading
#from.

#for i in students_period_A:
#  students_period_A.append(i)
#  print(i)

## Break ##

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for i in dog_breeds_available_for_adoption:
    print(i)
    if i == dog_breed_I_want:
        #stop loop iteration.
        break
print("They have the dog I want!")

## Continue ##

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

#Iterate through ages.
for i in ages:
    #Check if each item is less-than 21.
    if i < 21:
        #If it is less-than 21, continue interating.
        continue
    #Print the age as it is greater-than 21.
    print(i)

## While Loops ##

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

#The while loop runs until the length of 'students_in_poetry' is less-than 6.
while len(students_in_poetry) < 6:
    #remove the value using the last index and move forward in the list 'all_students'.
    add = all_students.pop()
    #Append to 'students_in_poetry'
    students_in_poetry.append(add)
    print(list(students_in_poetry))

#Output:
#['Loki']
#['Loki', 'Arius']
#['Loki', 'Arius', 'Obie']
#['Loki', 'Arius', 'Obie', 'Alexa']
#['Loki', 'Arius', 'Obie', 'Alexa', 'Minerva']
#'Loki', 'Arius', 'Obie', 'Alexa', 'Minerva', 'Dora']

## Nested Loops ##

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    print(list(location))
    for element in location:
        scoops_sold += element
        print(scoops_sold)

## List Comprehensions ##

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

for elem in heights:
    #Check if the elem in 'heights' is greater-than 161
    if elem > 161:
        #Add each element to a new list 'can_ride_coaster'
        can_ride_coaster = [elem]
        print(can_ride_coaster)

#Same thing as the above for loop in in a single line.
can_ride_coaster = [elem for elem in heights if elem > 161]

print(can_ride_coaster)

## More List Comprehensions ##

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp*(9/5) + 32 for temp in celsius]

print(fahrenheit)

## Review ##

#1. Create a list called single_digits that consists of the numbers 0-9 (inclusive)

#2. Create a for loop that goes through single_digits and prints out each one.

#3. Create a list called squares. Assign it to be an empty list to begin with.

#4. Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list #quares. You can do this before or after printing the element.

#5. After the for loop, print out squares.

#6. Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.

#7.Print cubes.

single_digits = range(0,10)

squares = []

for i in single_digits:
    squares.append(i**2)
    print(squares)

cubes = [i**3 for i in single_digits]
print (cubes)
