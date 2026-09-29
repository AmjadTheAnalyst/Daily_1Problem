# =====================================================================
# PYTHON MAP() FUNCTION: COMPREHENSIVE CHEAT SHEET FOR BEGINNERS
# =====================================================================
# Remember: map(function, iterable) returns a lazy iterator. 
# We wrap it in list() to print and view the final transformed elements.
# =====================================================================
# ---------------------------------------------------------------------
# 5. BONUS: TEXT TRANSFORMATIONS (upper, lower, title, etc.)
# ---------------------------------------------------------------------
# To use string methods inside map without a lambda, pass the method 
# directly from the string class (`str.upper`, `str.lower`, etc.).
# ---------------------------------------------------------------------
print("\n--- 5. Text Transformations ---")

raw_names = ["alice", "BOB", "charlie"]

# Convert all text to UPPERCASE
uppercase_names = list(map(str.upper, raw_names))
print(f"Uppercase Names:  {uppercase_names}")  # Output: ['ALICE', 'BOB', 'CHARLIE']

# Convert all text to lowercase
lowercase_names = list(map(str.lower, raw_names))
print(f"Lowercase Names:  {lowercase_names}")  # Output: ['alice', 'bob', 'charlie']

# Capitalize the first letter (Title case)
title_names = list(map(str.title, raw_names))
print(f"Title Case Names: {title_names}")  # Output: ['Alice', 'Bob', 'Charlie']

# Strip whitespace from messy text inputs
messy_strings = ["   hello ", "world   ", "  python  "]
cleaned_strings = list(map(str.strip, messy_strings))
print(f"Cleaned Strings:  {cleaned_strings}")  # Output: ['hello', 'world', 'python']

# ---------------------------------------------------------------------
# 1. TYPE CONVERSION FUNCTIONS
# ---------------------------------------------------------------------
print("--- 1. Type Conversion ---")

# Convert strings to integers
str_numbers = ["10", "20", "30"]
int_numbers = list(map(int, str_numbers))
print(f"Strings to Ints: {int_numbers}")  # Output: [10, 20, 30]

# Convert numbers to strings
mixed_types = [5, True, 3.14]
str_converted = list(map(str, mixed_types))
print(f"Items to Strings: {str_converted}")  # Output: ['5', 'True', '3.14']

# Convert values to their truthy/falsy Boolean state
raw_values = [0, "hello", "", []]
booleans = list(map(bool, raw_values))
print(f"Values to Bools: {booleans}")  # Output: [False, True, False, False]


# ---------------------------------------------------------------------
# 2. MATHEMATICAL & NUMERIC FUNCTIONS
# ---------------------------------------------------------------------
print("\n--- 2. Math & Numeric Functions ---")

# Get absolute (positive) values
negative_nums = [-5, 12, -100, 0]
absolute_nums = list(map(abs, negative_nums))
print(f"Absolute Values: {absolute_nums}")  # Output: [5, 12, 100, 0]

# Round decimals to the nearest integer
decimals = [1.2, 4.7, 9.5]
rounded_nums = list(map(round, decimals))
print(f"Rounded Values:  {rounded_nums}")  # Output: [1, 5, 10]


# ---------------------------------------------------------------------
# 3. METADATA & INFORMATION FUNCTIONS
# ---------------------------------------------------------------------
print("\n--- 3. Metadata & Information ---")

# Get lengths of different strings
words = ["apple", "hi", "python"]
word_lengths = list(map(len, words))
print(f"String Lengths: {word_lengths}")  # Output: [5, 2, 6]

# Get the exact data type of each item
mixed_list = [42, "hello", 3.14]
data_types = list(map(type, mixed_list))
print(f"Data Types:     {data_types}")  # Output: [<class 'int'>, <class 'str'>, <class 'float'>]


# ---------------------------------------------------------------------
# 4. SEQUENCE & COLLECTION TRANSFORMERS
# ---------------------------------------------------------------------
print("\n--- 4. Sequence & Collection Transformers ---")

# Sum up the numbers inside nested lists
nested_lists = [[1, 2], [10, 20, 30], [5]]
list_sums = list(map(sum, nested_lists))
print(f"Sums of Nested Lists: {list_sums}")  # Output: [3, 60, 5]

# Find the maximum value in each sub-list
list_maxes = list(map(max, nested_lists))
print(f"Max of Nested Lists:  {list_maxes}")  # Output: [2, 30, 5]


