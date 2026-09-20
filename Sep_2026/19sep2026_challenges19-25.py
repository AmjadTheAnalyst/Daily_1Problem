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
def find_second_largest(input_list):
    unique_input_list = [] #without using unique, sort can give wrong second number if first number is available more than 1 time.
    for number in input_list:
        if number not in unique_input_list:
            unique_input_list.append(number)
    unique_input_list.sort()
    return unique_input_list[-2]
value = find_second_largest(input_list)
print(value)

# 📝 FEEDBACK SUMMARY:
# ✅ Good use of lists, loops, and functions, with a clear approach to finding a second-largest value.
# 🔧 Main improvement: handle UNIQUE values and find the result without using sort(); track largest and second_largest while looping.
# ⭐ Score: 6/10

# ============================================================
# PYTHON CODING CHALLENGE 20
# OOP: Create a Student Class
# ============================================================
# GOAL:
# Create a simple Student class and create objects from it.
# This is your first OOP challenge.
#
# Focus on understanding:
# class
# object
# __init__
# self
# attributes
# methods
class Student():
    def __init__(self,name,age,course): #constructor
        self.name= name
        self.age= age
        self.course= course
    def introduce(self):
        print(self.name, self.age, self.course)
s1 = Student('Amjad',45,'BS Mathematics') #instance
s2 = Student('Ali',67,'BS Mathematics')
s1.introduce()
s2.introduce()

# 📝 FEEDBACK SUMMARY:
# ✅ Successfully created a Student class using **init**, self, attributes, objects, and methods.
# 💡 Strong first understanding of the core OOP structure and how objects store their own data.
# ⭐ Score: 9.5/10


#create a student class that takes name and marks of 3 sujects as arguments and then print average.
class Student():
    def __init__(self,name, marks): 
        self.name = name
        self.marks = marks
    def find_avg(self):
        average = sum(self.marks)/len(self.marks)
        print(average)
s1 = Student('Amjad',[12,43,67])
s2 = Student('Ali', [4,32,67])
#print(f'marks: {s1.marks} \nname: {s1.name}')
#print(s1.average)
s1.find_avg()
s2.find_avg()

# ============================================================
# PYTHON CODING CHALLENGE 21
# OOP: Student Marks Analyzer
# ============================================================
# GOAL:
# Improve your Student class by giving each student a list
# of marks and methods to analyze those marks.
class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def calculate_average(self):
        print(f'The average marks of {self.name} are: {(sum(self.marks))/(len(self.marks))}')
    def highest_mark(self):
        #print(f'The highest marks of {self.name} is: {max(self.marks)}')
        #The challenge specifically asked you to not use max() and to use a loop.
        #The purpose was to make you practice the algorithm yourself.
        largest = None
        for mark in self.marks:
            if largest is None or mark > largest:
                largest = mark
        print(f'The highest marks of {self.name} is: {largest}')
    def passed_subject(self):
        passed_marks = []
        for mark in self.marks:
            if mark >= 50:
                passed_marks.append(mark)
        print(f'Mr.{self.name} is passed in {len(passed_marks)} subjects')
s1 = Student('Amjad', [54,65,34])
s2 = Student('Ali', [45,67,98])
#print(s1.marks)
s1.calculate_average()
s2.highest_mark()
s1.passed_subject()

# 📝 FEEDBACK SUMMARY:
# ✅ Successfully combined OOP with lists, using **init**, self, attributes, methods, and loops correctly.
# 🔧 Main improvement: implement highest_mark() manually with a loop and start practicing returning values from methods.
# ⭐ Score: 8.5/10

# ============================================================
# PYTHON CODING CHALLENGE 22
# Find the Highest Temperature
# ============================================================

# GOAL:
# Create a TemperatureTracker class that finds the highest
# temperature from a list without using max().
class TemperatureTracker():
    def __init__(self,city,temperature):
        self.city= city
        self.temperature = temperature
    def highest_temperature(self):
        highest_temperature = None
        for temperature in self.temperature:
            if highest_temperature is None or temperature>highest_temperature:
                highest_temperature = temperature
        print(f'The highest temperature of {self.city} is {highest_temperature}')
city1 = TemperatureTracker("Berlin",[18, 21, 16, 24, 19, 27, 22])
city2 = TemperatureTracker("London",[15, 19, 17, 23, 20, 18, 25])

city1.highest_temperature()
city2.highest_temperature()

# 📝 FEEDBACK SUMMARY:
# ✅ Successfully implemented the "highest value so far" algorithm using a loop without max().
# 💡 Strong understanding of comparison, updating values, OOP, and list iteration.
# ⭐ Score: 9.5/10


# ============================================================
# PYTHON CODING CHALLENGE 23
# Find the Second Highest Score
# ============================================================

# GOAL:
# Create a GamePlayer class that finds the second highest
# UNIQUE score from a list.
class GamePlayer():
    def __init__(self,name,scores):
        self.name = name
        self.score = scores
    def second_highest_score(self):
        first_highest = None
        second_highest = None
        for score in self.score:
            if first_highest is None or score > first_highest:
                first_highest = score
        for score in self.score:
            if score < first_highest and (second_highest is None or score > second_highest):
                 second_highest = score 
        print(f'first highest score of {self.name} is {first_highest}')  
        print(f'second highest score of {self.name} is {second_highest}')
player1 = GamePlayer("Amjad",[85, 92, 78, 95, 92, 88]) 
player2 = GamePlayer("Ali",[70, 91, 84, 91, 76, 89])
print(player1.name)
player1.second_highest_score()
player2.second_highest_score()

#🟢 Pattern 3 — Top 2 / Top K: CLEARED ✅
#🎯 Score: 9.8/10
#💡 Correctly identified first and second highest while handling duplicate highest values.
#🚀 Next: Pattern 4 — Frequency / Counting


#...............................................................................................
# Pattern 4/15 — Frequency / Counting
# Challenge 24 — Count Player Scores
scores = [85, 92, 78, 92, 85, 92, 88, 78]
def count_scores(scores):
    score_frequency = {}
    for score in scores:
        if score in score_frequency:
            score_frequency[score] +=1
        else:
            score_frequency[score] =1
    return score_frequency
result_ready = count_scores(scores)
print(type(result_ready))
print(result_ready)

# Expected output:
# {85: 2, 92: 3, 78: 2, 88: 1}

#....................................................................................
# Pattern 4/15 — Frequency / Counting
# Challenge 25 — Count Product Purchases
#returns a dictionary showing how many times each product was purchased.
purchases = [
    "laptop",
    "mouse",
    "keyboard",
    "laptop",
    "mouse",
    "laptop",
    "headphones",
    "keyboard"
]
def count_purchases(purchases):
    purchase_frequency = {}
    for item in purchases:
        if item in purchase_frequency:
            purchase_frequency[item] += 1
        else:
            purchase_frequency[item] = 1
    return purchase_frequency
result = count_purchases(purchases)
print(result)

#✅ Challenge 25 — Frequency / Counting: Successfully implemented dictionary-based frequency counting without .count() or Counter.
#🧠 Demonstrated understanding of checking existing keys and updating their values correctly.
#🏆 Score: 10/10 | Pattern 4/15 — CLEARED
