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