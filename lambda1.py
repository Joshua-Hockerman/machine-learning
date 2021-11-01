import os

clear = lambda: os.system("cls")

# clear()

# remainder = lambda num: num % 2

# print(remainder(5))

# product = lambda x, y: x * y

# print(product(8, 32))


def testfunction(num):
    print(num)
    return lambda x: x * num


result10 = testfunction(10)

result100 = testfunction(100)

print(result10(9))

print(result100(9))


def myfunc(num):
    return lambda a: a * num


mydoubler = myfunc(2)
mytripler = myfunc(3)
myhalf = myfunc(0.5)

numbers_list = [2, 6, 8, 10, 11, 14, 3, 8, 4, 9, 5]

filtered_list = list(filter(lambda num: (num > 7), numbers_list))

print(filtered_list)


def addition(n):
    return n + n


numbers = [1, 2, 3, 4, 5]
result = map(addition, numbers)

print(list(result))

lam_result = map(lambda n: n + n, numbers)

print(list(lam_result))
