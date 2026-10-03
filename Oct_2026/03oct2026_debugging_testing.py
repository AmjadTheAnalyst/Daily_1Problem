#path lib Path
#Debugging and Testing
'''
cwd -- PythonPractice
relative dir -- PythonPractice/pathlib_test.py
You have this directory structure:
PythonPractice/pathlib_test.py
├── Sep_2026/
│   ├── data/
│   │   ├── students.csv
│   │   ├── sales.csv
│   │   ├── employees.txt
│   │   └── archive/
│   │       ├── old_students.csv
│   │       └── old_sales.csv
│   │
│   ├── reports/
│   │   ├── january.pdf
│   │   ├── february.pdf
│   │   └── summary.txt
│   │
│   ├── notes.txt
│   └── README.md
│
└── pathlib_test.py
'''

'''Task 1 — Create the Path
Create a Path object representing the Sep_2026 directory.
Then check whether:It exists.It is a directory.'''
from pathlib import Path
#1
path = Path('Sep2026')
print(path.exists())
print(path.is_dir())
#2
for item in path.iterdir():
    print(item)
#3
for file in path.glob('*.txt'):
    print(file)
#4
for file in path.glob('**.csv'):
    print(file)
#5
files = []
for file in path.glob('**.csv'):
    files.append(file)
print(f'Total .csv files are: {len(files)}')

#7
for file in path.rglob('*.pdf'):
    print(file)
#8
for item in path.iterdir():
    print(item)
#9
#it go and return all files inside mentioned folder irrespective of file type
#it gives the mentioned file type exactly in the mentioned folder.
#it gives the mentioned file type in and subfolders of mentioned folder.
#i will use .rglob('*.txt)
path = Path("Sep_2026/data/students.csv")
#Name: students.csv
print(path.name)
print(path.suffix)
print(path.stem)
print(path.exists())
print(path.is_file())

from pathlib import Path
for file in Path('Sep_2026').glob('*.py'):
    relative_path = file.relative_to(Path('Sep_2026'))
    print(relative_path)
