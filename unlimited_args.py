#addition
def add(*args): #keyword
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(5,4,8,10,55)
print()

#tuple
def tuple(*numbers):
    print(numbers[1])
    print(numbers)
    print(type(numbers))
tuple(4,5,6)