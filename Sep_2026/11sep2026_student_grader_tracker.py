#You are given a nested list containing student data. 
# Each sublist contains a student's name, their major, and a list of their exam scores.

students = [
    ["Alice", "Math", [80, 90, 85]],
    ["Bob", "History", [60, 70, 65]],
    ["Charlie", "Math", [95, 80, 80]],
    ["Diana", "Physics", [85, 85, 85]],
    ["Evan", "Computer Science", [70, 75, 80]]
]
"""Your Task Requirements:Calculate the Average: 
For each student, calculate their average exam score.
Filter: Include only students who have an average score of 75 or higher.
Sort the Output: The final list must be sorted:Primarily by their average score in descending order.
Secondarily by their name in alphabetical order (if their average scores are exactly the same).
Format: Format the final output strings exactly like this: "Name (Major) - Average: XX.X" (rounded to one decimal place)."""


avg_list = [
    f"{student[0]} ({student[1]}) - Average: {(sum(student[2])/len(student[2])):.1f}"
    for student in students
    if sum(student[2])/len(student[2]) >= 75 
]
print(avg_list)

#Pending work
#how to sort

#New Learnt
#f-strings in list comprehension
#lists dnt have exact avg function, we need to do it manually,
#lists also work on max, min, sum, len function,,, no need to convert into numeric values
