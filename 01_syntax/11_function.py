'''
def add(a, b):
    c = a+b
    print(c)


add(3, 2)
add(5, 7)


def add(a, b):
    c = a+b
    d = a-b
    return c, d


print(add(3, 2))
print(add(3, 2)[0])
'''

a = [12, 13, 7, 9, 19]


def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for x in a:
    if isPrime(x):
        print(x, end=' ')
