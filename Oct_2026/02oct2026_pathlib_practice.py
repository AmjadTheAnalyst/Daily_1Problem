#i created this file using Path object from another 01oct2026.py file
#from pathlib import Path
#Path('Oct_2026/02oct2026_pathlib_practice.py').touch()

#i want to print a list of all .py files available in Sep_2026 folder
from pathlib import Path
all_files = []
for file in Path('Sep_2026').glob('*.py'):
    print(file)
    all_files.append(file)
print(len(all_files))