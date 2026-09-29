with open('practice.txt', 'a+') as f:
    f.write('\nhow are you?')
    f.seek(0)
    data = f.read()
    print(data)
#WAF that replaces java with python
with open('practice.txt', 'r') as f:
    data = f.read()
new_data = data.replace('Java', 'python')
print(new_data)
#search if the word 'learning' exists or not in file
with open('practice.txt', 'r') as f:
    data = f.read()
    word = 'learning'
    if word in data:
        print(f'Yes,{word} is available')
    else:
        print(f'No,{word} is not available')

#WAF to check at which line it exactly available as the first occurance
def check_line_no():
    with open('practice.txt', 'r') as f:
        word = 'learning'
        line_number = 1
        check = True
        while check:
            data = f.readline()
            if word in data:
                return line_number
            line_number += 1
            if data == '':
                break
        return 'no word found'
a = check_line_no()
print(a)
                
#Problem 01:
def read_notes():
    with open('notes.txt', 'w+') as f:
        f.write('Python\nSQL\nMachine Learning\nDeep Learning')
        f.seek(0)
        data = f.read()
        return data
content = read_notes()
print(content)

#✅ Problem 01 — Text File Reading: Successfully opened a text file, wrote/read content, repositioned the file pointer with seek(), and returned the data.
#🧠 Key learning: Understand the difference between reading an existing file and using a write-capable mode that creates/overwrites the file.
#🏆 Score: 8.5/10 | Text File Handling — IN PROGRESS

#Problem 02:
def count_lines():
    with open('Sep_2026/students.txt', 'r') as f:
        data = True
        countl = 0
        while data :
            data = f.readline()
            if data == '':
                break
            else:
                countl +=1
        return countl
a = count_lines()
print(a)

#✅ Problem 02 — Count Lines: Correctly counted file lines using readline() and detected the end of the file with an empty string.
#🧠 Key learning: Demonstrated understanding of reading a text file line-by-line and using EOF detection to control a loop.
#🏆 Score: 9.5/10 | Text File Handling — IN PROGRESS


#Problem 03
#Return the total number of words in the file.
def count_words():
    with open('Sep_2026/articles.txt', 'r') as f:
        data = f.read()
        f.seek(0)
        new_words = data.split()
        return len(new_words)
a = count_words()
print(a)

#✅ Problem 03 — Count Words: Correctly read the complete text file, split the content into words, and returned the word count.
#🧠 Key learning: Demonstrated the difference between file reading and processing the resulting string with split().
#🏆 Score: 9.8/10 | Text File Handling — IN PROGRESS

#Problem 4
#Find a Specific Word
with open('Sep_2026/articles.txt', 'r') as f:
    data = f.read()
    specific_count = data.count('Python')
    print(specific_count)
#✅ Problem 04 — Find a Specific Word: Correctly read the text file and counted occurrences of the target text using str.count().
#🧠 Key learning: Demonstrated direct processing of file content after reading it, with no unnecessary function wrapper.
#🏆 Score: 10/10 | Text File Handling — IN PROGRESS


Name = input("Please enter your name: ")
Age = int(input("Please enter your age: "))
City = input("In which city you live: ")
with open('user.txt', 'w') as f:
    f.write(f'Name: {Name}\nAge: {Age}\nCity: {City}')

#✅ Problem 05 — Write User Data: Correctly collected user input and wrote formatted data to a text file using write mode and an f-string.
#🧠 Key learning: Demonstrated correct use of 'w' mode, newline characters, type conversion, and context-managed file writing.
#🏆 Score: 10/10 | Text File Handling — IN PROGRESS

#Problem 6
#Ask the user for a new task and append it to the file.
with open('Sep_2026/tasks.txt', 'a') as f:
    new_task = input('Please enter the new task: ')
    f.write(f'\n{new_task}')

#✅ Problem 06 — Append New Data: Correctly used append mode to add a new task to the existing text file without overwriting previous content.
#🧠 Key learning: Demonstrated the difference between write mode and append mode and correctly handled line separation.
#🏆 Score: 10/10 | Text File Handling — IN PROGRESS

#Problem 8
#Return a list containing students whose score is 80 or higher.
with open('Sep_2026/scores.txt', 'r') as f:
    data = f.readline()
    eligible_students = []
    while data:
        name, score = data.strip().split(',')
        if int(score) >= 80:
            eligible_students.append(name)
        data = f.readline()
    print(eligible_students)
#⚠️ Problem 08 — Filter Lines: Correctly read the file line-by-line, but the result list was reset inside the loop and scores were searched as strings instead of being parsed as numbers.
#🧠 Key learning: Read → parse → convert data type → apply condition. Also keep accumulated results outside the loop.
#🏆 Score: 6.5/10 | Text File Handling — IN PROGRESS