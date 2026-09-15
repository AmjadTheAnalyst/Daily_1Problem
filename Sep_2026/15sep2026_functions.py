#A function that calculates the sum of any number of values:
def summofvalues(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum
s = summofvalues(1,2,4,6)
print(s)

#A function that find the the max value
def max_value(*numbers):
    print(f"The maximum value is: {max(numbers)}")
print(max_value(1,2,3,4,5,6,7,8,9,10))

print(max((1,2,3,4)))

lis1 = [1,2,3,4]
print(lis1.pop())
print(lis1)

numbers = list(range(20))
print(numbers)