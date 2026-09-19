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