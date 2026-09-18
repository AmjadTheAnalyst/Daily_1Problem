# ============================================================
# PYTHON CODING CHALLENGE 19
# Find the Second Largest Number
# ============================================================

# GOAL:
# Write a Python program that takes a list of integers and
# finds the SECOND LARGEST UNIQUE number in the list.
#
# The program should return the second largest number.
#
# Do not simply use sorted() or sort() to solve the problem.
numbers = "473857538849999957"
input_list = []
for number in numbers:
    input_list.append(int(number))
def is_second_largest(input_list):
    unique_input_list = [] #without using unique, sort can give wrong second number if first number is available more than 1 time.
    for number in input_list:
        if number not in unique_input_list:
            unique_input_list.append(number)
    unique_input_list.sort()
    return unique_input_list[-2]
value = is_second_largest(input_list)
print(value)

# 📝 FEEDBACK SUMMARY:
# ✅ Good use of lists, loops, and functions, with a clear approach to finding a second-largest value.
# 🔧 Main improvement: handle UNIQUE values and find the result without using sort(); track largest and second_largest while looping.
# ⭐ Score: 6/10