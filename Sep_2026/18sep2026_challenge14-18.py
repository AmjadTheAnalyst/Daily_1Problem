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


# ============================================================
# PYTHON CODING CHALLENGE 15
# Find the Most Frequent Number
# ============================================================

# GOAL:
# Write a Python program that asks the user to enter 10 integers.
#
# The program should find which number appears the most times.
#
# Finally, display the most frequent number and how many times
# it appeared.

numbers = "2222747634" #input("Please enter 10 integers: ")
numbers_list = []
for number in numbers:    
    numbers_list.append(int(number))
def find_most_frequent(numbers_list):
    empty_dict = {}
    for number in numbers_list:
        empty_dict.update({number:numbers_list.count(number)})
    most_frequent_number = max(empty_dict, key = empty_dict.get)
    how_much_frequent = empty_dict.get(most_frequent_number)
    final_values = [most_frequent_number, how_much_frequent ]
    return final_values
returned_numbers = find_most_frequent(numbers_list)
print(f'which number is most frequent:{returned_numbers[0]} \nfrequency: {returned_numbers[1]}')
                                
'''Nice attempt — you're very close conceptually. Score: 8/10.
Good: You correctly built a dictionary of frequencies, used max(..., key=...) to find the most frequent number, 
and returned both the number and its frequency.
Needs improvement: You're using .count() inside the loop, which works but defeats 
the main goal of practicing a dictionary as a counter; also, *numbers_list* / *key* are not valid Python syntax 
(they look like formatting artifacts), and the function can return the two values more simply.'''






# ------------------------------------------------------------
# REQUIREMENTS:
# ------------------------------------------------------------

# 1. Store the 10 numbers in a list.

# 2. Create a function called find_most_frequent.

# 3. The function should receive the list as a parameter.

# 4. Use a dictionary to keep track of how many times each
#    number appears.

# 5. Use a for loop to process the numbers.

# 6. The function should return:
#       - the most frequent number
#       - how many times it appeared

# 7. If two or more numbers have the same highest frequency,
#    return the first one that reaches that frequency.

# 8. Add at least 2 meaningful comments.

# 9. Do not use external libraries.


# ------------------------------------------------------------
# EXAMPLE TEST CASES:
# ------------------------------------------------------------

# Test 1:
# Input:  2, 5, 2, 8, 5, 2, 3, 5, 2, 9
# Output: 2 appeared 4 times


# Test 2:
# Input:  1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# Output: 1 appeared 1 time


# Test 3:
# Input:  5, 5, 5, 2, 2, 3, 3, 3, 3, 8
# Output: 3 appeared 4 times


# Test 4:
# Input:  7, 7, 2, 2, 4, 4, 9, 9, 1, 1
# Output: 7 appeared 2 times


# ------------------------------------------------------------
# COACHING FOCUS:
# ------------------------------------------------------------

# This challenge is about using a DICTIONARY as a counter.
#
# Think:
#
# number → how many times have I seen it?
#
# Example:
#
# numbers = [2, 5, 2, 2]
#
# counts = {
#     2: 3,
#     5: 1
# }
#
# Then you need to find the number with the highest count.


# ------------------------------------------------------------
# IMPORTANT:
# ------------------------------------------------------------

# Try to solve it yourself first.
#
# Don't use collections.Counter.
#
# When you're finished, send me your code and I'll review it
# the same way as the previous challenges.

