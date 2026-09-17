# ============================================================
# PYTHON CODING CHALLENGE 8
# Count Even and Odd Numbers
# ============================================================

# GOAL
# Write a Python program that asks the user to enter 5 integers.
n1 = 1 #int(input("enter first number: ")) in same way user will enter all 5 numbers, i just entered manually
n2 = 3
n3 = 45
n4 = 5
n5 = 7
list = [n1,n2,n3,n4,n5]
even = []
odd = []
def count_even_odd(list):
    for number in list:
        if number % 2 == 0:
            even.append(number)
        elif number % 2 != 0:
            odd.append(number)
    return f"total even numbers are: {len(even)}" , f"total odd numbers are: {len(odd)}"
print(count_even_odd(list))
        
# - How many numbers are even
# - How many numbers are odd
#
# Finally, display both counts.

# CONSTRAINTS
# 1. Use input() to get the numbers.
# 2. Convert each input to an integer.
# 3. Store the numbers in a list.
# 4. Use a for loop to process the list.
# 5. Use a function called count_even_odd.
# 6. The function should receive the list as a parameter.
# 7. Use the modulo (%) operator to determine even and odd.
# 8. The function should return both counts.
# 9. Print the results outside the function.
# 10. Add at least 2 meaningful comments.
# 11. Do not use the built-in sum() function.
# 12. Do not use any external libraries.


#.............................................................................
# GOAL
# Write a Python program that asks the user to enter 5 numbers.
#
# Store the numbers in a list.
#
# Then create a function that finds and returns the largest
# number in the list.
#
# Do NOT use the built-in max() function.
#Do not use sorting methods such as sort() or sorted().
#Use a for loop inside the function.

n1 = 1 #int(input("enter first number: ")) in same way user will enter all 5 numbers, i just entered manually
n2 = 3
n3 = 45
n4 = 55
n5 = 7
list = [n1,n2,n3,n4,n5]
def find_largest(list):
    list.sort(reverse = True)
    return list[0]
print(find_largest(list))


# GOAL
# Write a Python program that asks the user to enter a sentence.
# The program should count how many vowels are present in the
# sentence. The vowels are:a, e, i, o, u
# The program should treat uppercase and lowercase vowels as the same.

characters = "i aAm a good boy" #input("Please type any sentence: ")
vowels = []
for char in characters:
    if char in ['a','A', 'e','E', 'i','I','o','O','u','U']:
        vowels.append(char)
#making a and A same, if user put both a and A i will count only one entry.
if 'a' in vowels and 'A' in vowels:
    vowels.remove('A')
if 'e' in vowels and 'E' in vowels:
    vowels.remove('E')
if 'i' in vowels and 'I' in vowels:
    vowels.remove('I')
if 'o' in vowels and 'O' in vowels:
    vowels.remove('O')
if 'u' in vowels and 'U' in vowels:
    vowels.remove('U')
print(f'Total vowels: {len(vowels)}')




characters = "i Am a good boy" #input("Please type any sentence: ")
vowels = []
def count_vowels(characters):
    for char in characters:
        if char in ['a','A', 'e','E', 'i','I','o','O','u','U']:
            vowels.append(char)
    return len(vowels)
a = count_vowels(characters)
print(a)
# 6. Spaces, numbers, and punctuation should not be counted.
# 7. Create a function called count_vowels.
# 8. The function should receive the sentence as a parameter.
# 9. The function should return the number of vowels.
# 10. Print the result outside the function.
# 11. Add at least 2 meaningful comments.
# 12. Do not use any external libraries.

#.........................................................................................................

# GOAL
# Write a Python program that asks the user to enter:
# 1. A sentence
# 2. A character
# The program should count how many times that character
# appears in the sentence.
sentence = "i am a good boy" #input("Please type any sentence: ")
character = "a" #input("Please type any character: ")
def character_count(sentence,character):
    character_counter = 0
    for char in sentence:
        if char == character:
            character_counter += 1  # Increases the count by 1
    return character_counter
total_count = character_count(sentence, character)
print(total_count)


# PYTHON CODING CHALLENGE 13
# Password Strength Checker
# GOAL
# Write a Python program that asks the user to enter a password.
#
# The program should check whether the password meets the
# following requirements:
#
# 1. At least 8 characters long
# 2. Contains at least one uppercase letter
# 3. Contains at least one lowercase letter
# 4. Contains at least one number
#
# If all requirements are met, print: Strong password
#Otherwise, print: Weak password

password = "sxknjcfb758re446"#input("Please enter any password")
def pass_checker(password):
    result = []
    if len(password) >= 8:
        result.append(True)
    else: result.append(False)
    has_upper = any(char.isupper() for char in password)
    if has_upper :
        result.append(True)
    else: result.append(False)
    has_lower = any(char.islower() for char in password)
    if has_lower == True:
        result.append(True)
    else: result.append(False)
    has_numeric = any(char.isdigit()for char in password)
    if has_numeric ==True:
        result.append(True)
    else: result.append(False)
    return result
conditions = pass_checker(password) 
if all(conditions): #returns only true if all conditions met
    print("Strong Password")
else:
    print("Weak Password")

password = "sxknjcfb758re446" #check if any letter is lower/upper

