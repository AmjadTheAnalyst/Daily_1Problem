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
