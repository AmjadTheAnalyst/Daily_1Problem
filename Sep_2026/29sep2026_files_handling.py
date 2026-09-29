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

