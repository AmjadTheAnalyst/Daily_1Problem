#create a student class that takes name and marks of 3 subject 
# and also print the average.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg_marks(self):
        print(f"Hi {self.name}, Your average marks are: {sum(self.marks)/len(self.marks)}")
s1 = Student("Amjad", [98,76,84])
s2 = Student("Ali", [99,89,76])
#print(s1.name, s2.name, s2.marks)
s1.avg_marks()
s2.avg_marks()