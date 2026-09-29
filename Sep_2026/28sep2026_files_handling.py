f = open('28sep2026_practice.txt', 'a+')
f.write('\nI am adding new lines')
f.seek(0)
data = f.read()
print(data)

with open('practice.txt', 'w') as f:
    data = f.write('Hi everyone\nWe are learning File I/O\nusing Java\nIlike programming in Java')
#write a program that replace java with python in above texct file
with open('practice.txt', 'r+') as f:
    data = f.read()
new_data = data.replace('Jave','Python')
print(new_data)

