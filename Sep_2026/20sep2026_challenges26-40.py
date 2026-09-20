#........................................................................................
# Pattern 5/15 — Seen / Duplicate Tracking
# Challenge 26 — Find Duplicate Products
products = [
    "laptop",
    "mouse",
    "keyboard",
    "laptop",
    "headphones",
    "mouse",
    "monitor",
    "keyboard",
    "mouse"
]
def find_duplicates(products):
    seen= set()
    duplicate_product = {}
    for product in products:
        if product in seen:
            duplicate_product[product]=1
        else: 
            seen.add(product)
    return duplicate_product
result = find_duplicates(products)
print(result.keys())

# Expected output:
# ["laptop", "mouse", "keyboard"]

#................................................................................
# Pattern 5/15 — Seen / Duplicate Tracking
# Challenge 27 — Find Duplicate Student IDs

student_ids = [
    101,
    205,
    302,
    101,
    410,
    205,
    512,
    302,
    205
]

def find_duplicate_ids(student_ids):
    seen = set()
    duplicate_ids = []
    for id in student_ids:
        if id in seen and id not in duplicate_ids :
         duplicate_ids.append(id)   
        else:
            seen.add(id)
    return duplicate_ids
result = find_duplicate_ids(student_ids)
print(result)

#✅ Challenge 27 — Seen / Duplicate Tracking: Correctly used a set to detect repeated student IDs and a list to store unique duplicates in order.
#🧠 Demonstrated complete understanding of the seen-set duplicate-tracking pattern in a new context.
#🏆 Score: 10/10 | Pattern 5/15 — CLEARED ✅

#.........................................................................................................................................................................
# Pattern 5/15 — Seen / Duplicate Tracking
# Challenge 28 — Find Repeated Email Addresses

emails = [
    "ali@gmail.com",
    "sara@gmail.com",
    "john@gmail.com",
    "ali@gmail.com",
    "maria@gmail.com",
    "sara@gmail.com",
    "david@gmail.com",
    "john@gmail.com",
    "sara@gmail.com"
]

def find_repeated_emails(emails):
    seen = set()
    duplicate_email = []
    for email in emails:
        if email in seen and email not in duplicate_email:
            duplicate_email.append(email)
        else:
            seen.add(email)
    return duplicate_email
result = find_repeated_emails(emails)
print(result)

# Expected output:
# ["ali@gmail.com", "sara@gmail.com", "john@gmail.com"]

#✅ Challenge 28 — Seen / Duplicate Tracking: Correctly identified repeated email addresses using a set and preserved unique duplicates in order.
#🧠 Demonstrated consistent mastery of the seen-set pattern across different contexts without using .count() or Counter.
#🏆 Score: 10/10 | Pattern 5/15 — CLEARED ✅

#........................................................................................................................................................
# Pattern 5/15 — Seen / Duplicate Tracking
# Challenge 29 — Find Repeated Book ISBNs

isbn_numbers = [
    "978-001",
    "978-045",
    "978-102",
    "978-078",
    "978-045",
    "978-210",
    "978-001",
    "978-330",
    "978-102",
    "978-045"
]

def find_repeated_isbn(isbn_numbers):
    seen = set()
    duplicated_isbn = []
    for isbn in isbn_numbers:
        if isbn in seen and isbn not in duplicated_isbn:
            duplicated_isbn.append(isbn)
        else:
            seen.add(isbn)
    return duplicated_isbn
result = find_repeated_isbn(isbn_numbers)
print(result)

# ✅ Challenge 29 — Seen / Duplicate Tracking: Correctly identified repeated ISBNs using a set while preserving unique duplicates in order.
#🧠 Demonstrated consistent mastery of duplicate tracking across multiple unrelated contexts.
#🏆 Score: 10/10 | Pattern 5/15 — CLEARED ✅



#.....................................................................................................................................................
# Pattern 6/15 — Filtering
# Challenge 30 — Filter Eligible Employees

employees = [
    {"name": "Ali", "age": 24},
    {"name": "Sara", "age": 31},
    {"name": "John", "age": 27},
    {"name": "Maria", "age": 19},
    {"name": "David", "age": 35},
    {"name": "Emma", "age": 22}
]
#Return the names of employees whose age is 25 or older.
def find_eligible_employees(employees):
    eligible_employees = []
    non_eligible_employees = []
    for employee in employees:
        if employee.get('age') >=25:
            eligible_employees.append(employee.get('name'))
        else:
            non_eligible_employees.append(employee.get('name'))
    return eligible_employees
result = find_eligible_employees(employees)
print(result)

#✅ Challenge 30 — Filtering: Correctly filtered employees based on age and returned only the qualifying names in order.
#🧠 Demonstrated the core filtering pattern using a condition, loop, list, and dictionary access; only minor cleanup was needed.
#🏆 Score: 9.8/10 | Pattern 6/15 — IN PROGRESS


#....................................................................................................................................
# Pattern 6/15 — Filtering
# Challenge 31 — Filter Available Products
products = [
    {"name": "Laptop", "stock": 12},
    {"name": "Mouse", "stock": 0},
    {"name": "Keyboard", "stock": 7},
    {"name": "Monitor", "stock": 0},
    {"name": "Headphones", "stock": 15},
    {"name": "Webcam", "stock": 3}
]
#Return the names of products that are currently in stock.
def find_available_products(products):
    available_products = []
    not_available_products = []
    for product in products:
        if product.get('stock') != 0 and product.get('name') not in available_products:
            available_products.append(product.get('name'))
        else:
            not_available_products.append(product.get('name'))
    return available_products
result = find_available_products(products)
print(result)

# ✅ Challenge 31 — Filtering: Correctly filtered available products using a stock condition and returned their names in order.
#🧠 Demonstrated the core filtering pattern independently in a new context; minor cleanup and a more precise > 0 condition would improve the solution.
#🏆 Score: 9.7/10 | Pattern 6/15 — IN PROGRESS

#............................................................................................................................................................
students = [
    {"name": "Ali", "marks": 78, "attendance": 85},
    {"name": "Sara", "marks": 91, "attendance": 92},
    {"name": "John", "marks": 64, "attendance": 88},
    {"name": "Maria", "marks": 83, "attendance": 72},
    {"name": "David", "marks": 95, "attendance": 96},
    {"name": "Emma", "marks": 88, "attendance": 79}
]
#A student is qualified only if:
#marks are 80 or higher
#and attendance is 80 or higher
# Return only the qualified students' names.

def find_qualified_students(students):
    qualified_students = []
    for student in students:
        if student.get('marks') >= 80 and student.get('attendance')>=80:
            qualified_students.append(student.get('name'))
    return qualified_students
result = find_qualified_students(students)
print(result)

# ✅ Challenge 32 — Filtering: Correctly filtered students using two conditions with AND and returned only qualified names.
# 🧠 Demonstrated strong understanding of compound filtering logic and applied the pattern correctly in a new context.
# 🏆 Score: 10/10 | Pattern 6/15 — IN PROGRESS

#.................................................................................................................................
transactions = [
    {"id": 101, "type": "credit", "amount": 250},
    {"id": 102, "type": "debit", "amount": 80},
    {"id": 103, "type": "credit", "amount": 120},
    {"id": 104, "type": "debit", "amount": 300},
    {"id": 105, "type": "credit", "amount": 450},
    {"id": 106, "type": "credit", "amount": 90}
]
#Return the transaction IDs where:
#type is "credit"
#AND amount is greater than 200
def find_large_credits(transactions):
    qualified_transactions = []
    for transaction in transactions:
        if transaction.get('type') == 'credit' and transaction.get('amount')>200:
            qualified_transactions.append(transaction.get('id'))
    return qualified_transactions 
result = find_large_credits(transactions)
print(result)

# ✅ Challenge 33 — Filtering: Correctly filtered credit transactions above the required amount and returned their IDs in order.
# 🧠 Demonstrated consistent mastery of single and compound filtering conditions across different contexts.
# 🏆 Score: 10/10 | Pattern 6/15 — IN PROGRESS

#........................................................................................................................................
files = [
    "report.pdf",
    "photo.jpg",
    "data.csv",
    "notes.txt",
    "presentation.pdf",
    "script.py",
    "summary.pdf",
    "image.png"
]

def find_pdf_files(files):
    pdf_files = []
    for file in files:
        if file.endswith('.pdf'):
            pdf_files.append(file)
    return pdf_files
result = find_pdf_files(files)
print(result)

# ✅ Challenge 34 — Filtering: Correctly filtered PDF files using a string condition and preserved the original order.
# 🧠 Demonstrated consistent mastery of the filtering pattern across numeric, dictionary, compound, and string-based conditions.
# 🏆 Score: 10/10 | Pattern 6/15 — CLEARED ✅

#......................................................................................................................................
# Pattern 7/15 — Building Result Lists
# Challenge 35 — Convert Celsius to Fahrenheit

celsius_temperatures = [0, 10, 20, 25, 30, 40]
#F = (C × 9/5) + 32
def convert_to_fahrenheit(celsius_temperatures):
    fahrenheit_temperatures = []
    for temperature in celsius_temperatures:
        converted_temperature = (temperature * 9/5) + 32
        fahrenheit_temperatures.append(converted_temperature)
    return fahrenheit_temperatures
result = convert_to_fahrenheit(celsius_temperatures)
print(result)

# ✅ Challenge 35 — Building Result Lists: Correctly transformed each Celsius value into Fahrenheit and built a new result list while preserving order.
# 🧠 Demonstrated clear understanding of transforming every input item into a new output value rather than filtering items.
# 🏆 Score: 10/10 | Pattern 7/15 — IN PROGRESS
#...................................................................................................................................................................
# Pattern 8/15 — Searching
# Challenge 36 — Find a Product by Name

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 35},
    {"name": "Keyboard", "price": 80},
    {"name": "Monitor", "price": 300},
    {"name": "Headphones", "price": 150}
]
#Search for the product whose "name" matches product_name.
#Return the complete product dictionary when found.
#If the product does not exist, return None.
def find_product(products, product_name):
    final_result = ''
    for product in products:
        if product.get('name') == product_name:
            final_result = product
        else:
            final_result = None
    return final_result
result = find_product(products, "Monitor")

print(result)

# ✅ Challenge 36 — Searching: Correctly identified the target product, but the else branch can overwrite a previously found result.
# 🧠 Key lesson: return immediately when the target is found, then return None only after the entire search finishes without a match.
# 🏆 Score: 9.5/10 | Pattern 8/15 — IN PROGRESS

#.................................................................................................................................................
# Pattern 8/15 — Searching
# Challenge 37 — Find Student by ID

students = [
    {"id": 101, "name": "Ali", "major": "Mathematics"},
    {"id": 205, "name": "Sara", "major": "Computer Science"},
    {"id": 302, "name": "John", "major": "Physics"},
    {"id": 410, "name": "Maria", "major": "Data Science"},
    {"id": 512, "name": "David", "major": "Engineering"}
]
#Search for the student whose "id" matches student_id.
#Return the complete student dictionary when found.
#If the ID doesn't exist, return None.
def find_student(students, student_id):
    for student in students:
        if student.get('id') == student_id:
            return student
    return None
         
result = find_student(students, 678)

print(result)

# ✅ Challenge 37 — Searching: Correctly searched for a student by ID, returned immediately when found, and handled missing IDs with None.
# 🧠 Demonstrated complete understanding of the Search → Find → Return pattern after correcting the previous overwrite issue.
# 🏆 Score: 10/10 | Pattern 8/15 — IN PROGRESS
#......................................................................................................................................



#🟢 Pattern 8/15 — Searching
#Challenge #38 — Find a Flight Destination
#You have a list of flight records. Write a function that searches for a flight using its flight number.
flights = [
    {"flight": "LH401", "destination": "New York", "gate": "B12"},
    {"flight": "BA902", "destination": "London", "gate": "A07"},
    {"flight": "AF123", "destination": "Paris", "gate": "C21"},
    {"flight": "EK202", "destination": "Dubai", "gate": "D05"},
    {"flight": "SQ321", "destination": "Singapore", "gate": "E14"}
]
def find_flight(flights, flight_number):
    for flight in flights:
        if flight.get('flight') == flight_number:
            return flight
    return None
result = find_flight(flights,'SQ321')
print(result)

#✅ Challenge 38 — Searching: Correctly searched flight records by flight number and returned the matching dictionary immediately.
#🧠 Demonstrated complete understanding of the Search → Match → Return pattern, including None when no match exists.
#🏆 Score: 10/10 | Pattern 8/15 — CLEARED ✅

#...................................................................................................
#🔵 Pattern 9/15 — Two-List Comparison
#Challenge #39 — Match Students with Their Assigned Courses

students = [
    {"id": 101, "name": "Ali"},
    {"id": 102, "name": "Sara"},
    {"id": 103, "name": "David"},
    {"id": 104, "name": "Maria"}
]

enrollments = [
    {"student_id": 103, "course": "Machine Learning"},
    {"student_id": 101, "course": "Python"},
    {"student_id": 104, "course": "SQL"},
    {"student_id": 102, "course": "Deep Learning"}
]
#Requirements
#For every student in students:
#Look through enrollments.
#Find the enrollment whose student_id matches the student's id.
#Create a new dictionary containing:
#"name"
#"course"
#Add that dictionary to a result list.
#Return the final result list.
def get_student_courses(students, enrollments):
    name_enrollment = []
    for student in students:
        for enrollment in enrollments:
            if student.get('id') == enrollment.get('student_id'):
                new_data = {'name': student.get('name'), 'course': enrollment.get('course')}
                name_enrollment.append(new_data)
    return name_enrollment
result = get_student_courses(students, enrollments)
print(result)
#✅ Challenge 39 — Two-List Comparison: Correctly compared student IDs with enrollment IDs using nested loops.
#🧠 Core comparison logic was correct; main improvement is distinguishing a set from a key-value dictionary when building results.
#🏆 Score: 9/10 | Pattern 9/15 — IN PROGRESS
#[{'Python', 'Ali'}, {'Deep Learning', 'Sara'}, {'David', 'Machine Learning'}, {'Maria', 'SQL'}]

#..............................................................................................................................
#🔵 Pattern 9/15 — Two-List Comparison
#Challenge #40 — Match Products with Warehouse Stock

products = [
    {"product_id": 201, "name": "Laptop"},
    {"product_id": 202, "name": "Keyboard"},
    {"product_id": 203, "name": "Monitor"},
    {"product_id": 204, "name": "Mouse"}
]

warehouse = [
    {"id": 203, "stock": 12},
    {"id": 201, "stock": 5},
    {"id": 204, "stock": 30},
    {"id": 202, "stock": 18}
]
def get_product_stock(products, warehouse):
    new_list = []
    for product in products:
        for warehouse_item in warehouse:
            if product["product_id"] == warehouse_item["id"]:
                new_dict = {'name': product.get('name'), 'stock':warehouse_item.get('stock') }
                new_list.append(new_dict)
    return new_list
result = get_product_stock(products, warehouse)
print(result)

#✅ Challenge 40 — Two-List Comparison: Correctly matched products with warehouse records using nested loops and matching IDs.
#🧠 Successfully built the required dictionary result after correcting the set-vs-dictionary issue from the previous challenge.
#🏆 Score: 10/10 | Pattern 9/15 — CLEARED ✅