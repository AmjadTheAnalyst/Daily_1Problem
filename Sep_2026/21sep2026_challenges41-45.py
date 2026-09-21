#🔟 Pattern 10/15 — Nested Loops
#Challenge 41 — Find Common Seat Numbers
event_a = [101, 205, 310, 405, 502]
event_b = [205, 310, 410, 502, 601]
def find_common_seats(event_a, event_b):
    common_seats = []
    for event1 in event_a:
        for event2 in event_b:
            if event1 == event2 and event1 not in common_seats:
                common_seats.append(event1)
    return common_seats
result = find_common_seats(event_a, event_b)
print(result)

#✅ Challenge 41 — Nested Loops: Correctly compared both event lists using nested loops and returned unique matching seats in event_a order.
#🧠 Demonstrated solid control of nested iteration, matching conditions, duplicate prevention, and result construction.
#🏆 Score: 10/10 | Pattern 10/15 — IN PROGRESS