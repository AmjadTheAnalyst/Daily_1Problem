# ============================================================
# PYTHON CODING CHALLENGE 14
# Find Duplicate Numbers
# ============================================================

# GOAL:
# Write a Python program that asks the user to enter 8 integers.
#
# The program should find which numbers appear more than once.
#
# Finally, display the duplicate numbers.


# ------------------------------------------------------------
# REQUIREMENTS:
# ------------------------------------------------------------

# 1. Store the 8 numbers in a list.

# 2. Create a function called find_duplicates.

# 3. The function should receive the list as a parameter.

# 4. Use a set to keep track of numbers you have already seen.

# 5. Use another set to keep track of duplicate numbers.

# 6. Use a for loop.

# 7. The function should return the duplicate numbers.

# 8. Do not use a dictionary.

# 9. Do not use collections.Counter.

# 10. Add at least 2 meaningful comments.

# 11. Do not use external libraries.

numbers = '634577' #input("Please enter 8 numbers: ")
'''numbers_list = []
for number in numbers:    
    numbers_list.append(number)
print(numbers_list)'''
duplicated = set()
non_duplicate = set()
for number in numbers:
    if numbers.count(number) > 1:
        duplicated.add(number)
if len(duplicated) == 0:
    print("No duplicate found")
else:
    print(f'duplicated: {duplicated}')


#...using function 
numbers = '6734589' #input("Please enter 8 numbers: ")
numbers_list = []
for number in numbers:    
    numbers_list.append(int(number))
#print(numbers_list) [6, 7, 3, 4, 5, 7, 5, 7]
def find_duplicates(numbers_list):
    seen = set()
    duplicate_value = set()
    for number in numbers_list:
        if number in seen:
            duplicate_value.add(number)
        else:
            seen.add(number)
    return duplicate_value
returned_duplicated = find_duplicates(numbers_list)
if len(returned_duplicated) == 0:
    print("No duplicates")
else:
    print(returned_duplicated)

#AI Feedback 
#Score: 8/10
'''Your logic worked, you used functions, loops, lists, and sets correctly, and your duplicate detection handled repeated values well.
Needs improvement: You used .count() instead of the intended seen + duplicates approach, and your non_duplicate set wasn't necessary.
'''

