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