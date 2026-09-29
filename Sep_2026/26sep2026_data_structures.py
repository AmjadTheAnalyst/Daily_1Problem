list = [[1,2,3],[4,5,6],[7,8,9]]

one_list = [
    one_item
    for item in list
        for one_item in item
]
print(one_list)
#generate a list of all possible divisors of number
number = 36
divisors_list = [
    n
    for n in range(1,37)
    if number % n == 0
]
print(divisors_list)