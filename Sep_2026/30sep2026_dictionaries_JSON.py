a = {"name": "Bob", "role": "Agent"}
for element in a:
    print(element)

'''4. Dynamic Presence Check (Level: Medium)
The Scenario: You receive a raw response dictionary from an LLM API:
ai_response = {"action": "search", "query": "Python tutorials"}
The Task: Write a validation step using an if statement to check if the key "destination" is inside the dictionary. 
If it is missing, print a meaningful error message telling the user exactly what is missing.
'''

ai_response = {"action": "search", "query": "Python tutorials"}
#"destination"
if "destination" not in ai_response.keys():
        print('The information regarding destination is missing')

keys_list = ["username", "email", "id"]
values_list = ["ai_dev", "dev@agent.ai", 404]

#...............
from pathlib import Path
#introducted in python 3.4
path = Path.cwd() #Path is a smart object which indicates file and folder names as an object instead of strings
print(path)
from pathlib import Path
home_d = Path.home()
print(home_d)

#.............
from pathlib import Path
base = Path('Project')
file_path = base / 'data' /'day1' /'30sep2026.py'
print(file_path)
from pathlib import Path
main_dir = Path(__file__).resolve().parent
print(main_dir)

from pathlib import Path
a = Path(__file__).parent
print(a)

from pathlib import Path
p = Path('Sep_2026/10sep2026_data_filteration_using_listcomprehension.py') #worked
print(p.exists())
#why this not working
p = Path('10sep2026_data_filteration_using_listcomprehension.py') #for exists it saying Fasle



from pathlib import Path
print(Path(__file__).resolve().name)

#---------------------------------------------------
'''🟢 Problem 01 — Explore a Folder

Assume you have this folder:

Sep_2026/
├── scores.txt
├── students.csv
├── notes.txt
├── report.pdf
├── data.csv
└── images/
    ├── photo1.jpg
    └── photo2.png

Write Python code using pathlib to:
Create a Path object for Sep_2026.
Check whether the folder exists.
Print all items directly inside Sep_2026.
Print only the .txt files.
For each .txt file, print its filename and whether it is a file.'''
from pathlib import Path
required_wd = Path('Sep_2026')
print(required_wd.is_dir()) 
for file in required_wd.glob('*.txt'):
    print(file)

for file in required_wd.glob('*.txt'):
    print(file.name)
    if file.is_file():
        print(f'yes {file} is a file')
    else:
        print(f'{file} is not a file')

from pathlib import Path
cwd = Path(__file__).resolve().parent.name
print(cwd)

#output
import pandas as pd  
#with open('Sep_2026/EQUITY_L.csv', 'r') as file:
data = pd.read_csv('Sep_2026/EQUITY_L.csv' , sep=',')
print(data.shape)