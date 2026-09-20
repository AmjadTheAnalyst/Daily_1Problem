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
