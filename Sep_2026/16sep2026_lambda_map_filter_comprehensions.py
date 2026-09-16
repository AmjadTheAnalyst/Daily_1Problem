
# ============================================================
# PYTHON CODING CHALLENGE
# Positive, Negative, or Zero
# ============================================================

# GOAL 01
# Write a Python program that asks the user to enter a number
# and determines whether the number is:
# - Positive
# - Negative
# - Zero

# EXPECTED OUTPUT
# Print exactly one of:
#
# Positive
# Negative
# Zero

number = float(input('Please enter any number: '))
#An integer is a whole number that can be positive, negative, or zero
if number >0:
    print("Positive")
if number <0:
    print("Negative")
if number == 0:
    print("Zero")


# GOAL 02
# Write a Python program that asks the user to enter an integer
# and determines whether the number is even or odd.
number = float(input("Please enter any number: "))
if number % 2 == 0:
    print(f'{number} is an even number.')
else:
    print(f'{number} is an odd number.')



# GOAL 3 -- Simple Grade Calculator
# Write a Python program that asks the user to enter a test
# score and determines the student's grade.


# INPUT
# Ask the user to enter a score between 0 and 100.
score = int(input("Please enter the score between 0 and 100: "))
#i will also check whether score is entered between provided range
if score not in range(1,101):
    print("Please enter score between 0 and 100 only")
elif score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
elif score >= 50:
    print("Grade E")
else:
    print("Grade F")



# GOAL 4 -- Number Analyzer
# Write a Python program that asks the user to enter an integer.
#
# The program should determine:
# 1. Whether the number is positive, negative, or zero.
# 2. Whether the number is even or odd.
#
# Then print both results.
number = int(input("Please enter any integer: "))
if number >0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else: 
    print("The number is zero.")
if number % 2 == 0:
    print('The number is even.')
else:
    print('The number is odd.')



# GOAL 5 -- Simple Calculator
# Write a Python program that works as a simple calculator.
#
# The program should:
# 1. Ask the user for two numbers.
# 2. Ask the user which operation they want to perform.
# 3. Perform the selected operation.
# 4. Display the result.

a = int(input("please enter first number: "))
b = int(input("please enter second number: "))
c = input("Please enter your desired operation(+,-,*,/): ")
possible_operators = ['+', '-', '*', '/']
print(f"You want to perform {c} operation on {a} and {b}.")
if c == '+': #i will check strings but perform actual method in print
    print(f'{a}+{b}') 
elif c == '-':
    print(f'{a}-{b}')
elif c == '*':
    print(f'{a}*{b}')
else:
    print(f'{a}/{b}')


#i did not know how to deal with data types of operators.
#i made {a}operator{b}, which is wrong
#i did not know , how to divide two numbers



# GOAL -- 6 Function-Based Addition Calculator
# Write a Python program that:
#
# 1. Asks the user for two numbers.
# 2. Uses a function to add the two numbers.
# 3. Displays the result.
a = int(input("please enter first number: "))
b = int(input("please enter second number: "))
def addition(a,b):
    return(a+b)
print(addition(a,b))

# GOAL 07
# Write a Python program that works as a simple calculator.
#
# The program should:
# 1. Ask the user for two numbers.
# 2. Ask the user to select an operation.
# 6. Return the calculated result from the function.
# 7. If the operation is invalid, return:
#
#    Invalid operation
#
# 8. If the user tries to divide by zero, return:
#
#    Cannot divide by zero
#
# 9. Call the function from your main program.
# 10. Add at least 2 meaningful comments.
# 11. Do not use loops.
# 12. Do not use lists, dictionaries, or sets.

a = float(input("please enter first number: "))
b = float(input("please enter second number: "))
c = input("Please enter your desired operation(+,-,*,/): ")

def calculate(a,b,c):
    if c not in ('+','-','*','/'): #checking for valid operation
        return "Invalid operation"
    elif c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    elif c == '/':
        if b == 0: #making sure it not divided by 0
            return f"{a} can not be divided by 0"
        else:
            return a/b       
print(calculate(a,b,c))

##return f"Error: {a} cannot be divided by 0"



















#..............
#Map Function (use for comprehensions)
list1 = ["a", "b", "c", "d"]
#change all to upper case
#method 1 
for ch in list1:
    print(ch.upper())
#return list
list2 = []
for ch in list1:
    list2.append(ch.upper())
print(list2)
#method 2 with map function
list1 = ["a", "b", "c", "d"]
print(list(map(str.upper,list1)))

#enumerate function
list1 = ["a", "b", "c", "d"]
#list(enumerate(list1))
for num , val in list(enumerate(list1)):
    print(num, val)

#what if i want to filter out my list, lets say i need only numeric values
list1 = ["a", "b", "c", "d","1"]
print(list(filter(str.isalpha, list1)))


l1 = [1,2,3,4,5,6]
l2 = ['amjad', 'ali', 'shahzad', 'maria', 'shehzadi', 'zubair']
#print(l1+l2)
#print(l1*2)
#print(list(zip(l2,l1)))
for name, id in zip(l2,l1):
    print(name, id)

l1 = [1,2,3,4,5,6]
for id, index in enumerate(l1):
    print(id, index)

l2 = ['amjad', 'ali', 'shahzad', 'maria', 'shehzadi', 'zubair']
print(list(map(lambda x : x.startswith('a'), l2)))




#question1
'''You have a list of prices as strings, 
but they all have a dollar sign ($) in front of them.
convert this list into a list of floating-point numbers (floats) so you can do math with them.'''
prices = ["$10.99", "$5.50", "$21.00", "$0.99"]
cleaned = []
#method1 #manual
for price in prices:
    #"$10.99"
    cleaned.append(float(price.replace('$','')))
print(cleaned)
print(type(cleaned[0]))

#method2 #mapfunction
prices = ["$10.99", "$5.50", "$21.00", "$0.99"]
print(list(map(lambda x: float(x.replace('$','')),prices)))



#question2
#extract only the ages that are 18 or above.
ages = [14, 25, 17, 18, 42, 12, 31]
age18 = []
#method1 -- manual
for age in ages:
    if age >= 18:
        age18.append(age)
print(age18)


ages = [14, 25, 17, 18, 42, 12, 31]
#method2 -- filter function
print(list(filter(lambda x: x>=18, ages)))


#question3
movies = [
    {"title": "Inception   ", "rating": 8.8},
    {"title": "The Room", "rating": 3.7},
    {"title": "Interstellar ", "rating": 8.6},
    {"title": "Cats", "rating": 2.8},
    {"title": "The Matrix    ", "rating": 8.7}
]

#extract and clean the titles of only the movies 
#having a rating of 8.0 or higher.
cleaned_movies = [
    movie["title"].strip()
    for movie in movies
    if movie["rating"] >= 8.0
]
print(cleaned_movies)