# ==============================================================================
# 🐍 DAY 1 CHALLENGE: THE TIP & SPLIT CALCULATOR
# ==============================================================================
#
# COURSE RETROSPECTIVE: Practice User Input, Type Conversion, and Math Operations.
#
# THE SCENARIO:
# You and your friends went out to eat. You need to calculate how much each 
# person should pay, including the tip.
#
# YOUR TASK:
# 1. Ask the user for the total bill amount (e.g., 100).
# 2. Ask for the tip they want to leave.
# 3. Ask for the number of people splitting the bill (e.g., 4).
# 4. Calculate the final amount each person needs to pay.
# 5. Print the final result formatted to 2 decimal places.
#
# WRITE YOUR CODE BELOW THIS LINE:
# ==============================================================================

total_bill = int(input("total amount: "))
tip = int(input("tip if any: "))
no_of_people = int(input("number of people splitting: "))
amount = (total_bill + tip)/no_of_people
print(f"Each Person shares: {amount:.4f}")

#my new learning
#i learnt how to make format result upto specific decimal places
#i write int in input , so i should write float to accept float prices possibly.


#When you write print(f"{each_person:.2f}"), 
# you are breaking it into a specific formula:f"...": 
# The letter f tells Python, "Look inside this text for curly braces {} 
# and evaluate the code inside them.
# "each_person: This is the variable holding your calculated number.
# : (The Colon): This is the separator. 
# It tells Python, "Everything after this colon is a rule for how to style/format the number."
# .2: This specifies how many digits to display after the decimal point.
# f: This stands for Float (floating-point number).
#  It tells Python to treat the value as a decimal number.
