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

#...........................................................................................................
menu_a = ["Pizza", "Burger", "Pasta"]
menu_b = ["Pasta", "Salad", "Pizza", "Soup"]
#Find dishes that appear in both menus.
#Do not include duplicates in the result.
def find_common_dishes(menu_a, menu_b):
    common_dishes = []
    for dish_a in menu_a:
        for dish_b in menu_b:
            if dish_a == dish_b and dish_a not in common_dishes:
                common_dishes.append(dish_a)
    return common_dishes

result = find_common_dishes(menu_a, menu_b)
print(result)
#✅ Challenge 42 — Nested Loops: Correctly found common dishes using nested loops while preserving order and preventing duplicates.
#🧠 Demonstrated that the nested-loop comparison pattern transfers correctly to a completely different context.
#🏆 Score: 10/10 | Pattern 10/15 — IN PROGRESS