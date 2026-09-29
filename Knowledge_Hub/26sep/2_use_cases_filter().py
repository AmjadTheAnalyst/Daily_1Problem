# =====================================================================
# PYTHON FILTER() FUNCTION: COMPREHENSIVE CHEAT SHEET FOR BEGINNERS
# =====================================================================
# Remember: filter(function, iterable) returns a lazy iterator.
# It only KEEPS items where the function returns True (or a truthy value).
# We wrap it in list() to print and view the final filtered elements.
# =====================================================================
# ---------------------------------------------------------------------
# 3. TEXT & STRING METHOD FILTERS
# ---------------------------------------------------------------------
# You can use built-in string methods that return True or False 
# (like .isdigit, .isalpha, .islower, .isupper) to filter text.
print("\n--- 3. Text Filters (String Methods) ---")

user_inputs = ["123", "abc", "456", "hello12", "789"]

# Keep ONLY strings that contain purely numbers
numeric_strings = list(filter(str.isdigit, user_inputs))
print(f"Pure Numbers:     {numeric_strings}")  # Output: ['123', '456', '789']

# Keep ONLY strings that contain purely alphabet letters
alphabet_strings = list(filter(str.isalpha, user_inputs))
print(f"Pure Letters:     {alphabet_strings}")  # Output: ['abc']

mixed_cases = ["APPLE", "banana", "CHERRY", "date"]

# Keep ONLY uppercase words
uppercase_words = list(filter(str.isupper, mixed_cases))
print(f"Uppercase Words:  {uppercase_words}")  # Output: ['APPLE', 'CHERRY']
# ---------------------------------------------------------------------
# 1. THE ULTIMATE TRUTH FILTER: Passing `None`
# ---------------------------------------------------------------------
# If you pass `None` as the first argument, filter() automatically
# uses Python's built-in truth rules to drop all "Falsy" values 
# (like 0, empty strings, empty lists, and None).
print("--- 1. Removing Falsy Values (None Filter) ---")

messy_data = [42, 0, "hello", "", True, False, [], None, {"key": "val"}]
valid_data = list(filter(None, messy_data))
print(f"Cleaned Data: {valid_data}")  
# Output: [42, 'hello', True, {'key': 'val'}] -> Drops 0, "", False, [], and None!


# ---------------------------------------------------------------------
# 2. BOOLEAN TYPE FILTER
# ---------------------------------------------------------------------
# Using `bool` behaves similarly to passing `None`, keeping only items 
# that evaluate to True.
print("\n--- 2. Boolean Filter ---")

scores = [100, 0, 85, 0, 92]
active_scores = list(filter(bool, scores))
print(f"Non-zero Scores: {active_scores}")  # Output:  -> Drops the zeros





# ---------------------------------------------------------------------
# 4. SEQUENCE & METADATA FILTERS
# ---------------------------------------------------------------------
# Filter collections based on their inner properties.
print("\n--- 4. Sequence & Metadata Filters ---")

# Keep only sub-lists that have AT LEAST one True or non-zero value
nested_lists = [[0, 0], [1, 0], [0, False], [5, 6]]
active_lists = list(filter(any, nested_lists))
print(f"Lists with data:  {active_lists}")  # Output: [, ]

# Keep only sub-lists where EVERY single element is True or non-zero
perfect_lists = list(filter(all, nested_lists))
print(f"Perfect Lists:    {perfect_lists}")  # Output: []


# =====================================================================
# 💡 THE MODERN PYTHONIC CHEAT SHEET FOR FILTER
# =====================================================================
# Just like map(), modern Pythonistas prefer List Comprehensions 
# over filter() when writing complex logic or using lambda.
#
# Filter style:             list(filter(str.isdigit, words))
# List Comprehension style: [w for w in words if w.isdigit()]
# =====================================================================
