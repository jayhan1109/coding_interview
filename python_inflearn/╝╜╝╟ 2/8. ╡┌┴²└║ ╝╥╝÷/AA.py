N = int(input())
arr = list(map(int, input().split()))


def reverse(num):
    s = list(str(num))
    p = 0
    q = len(s) - 1

    while p < q:
        s[p], s[q] = s[q], s[p]
        p += 1
        q -= 1

    return int(''.join(s))


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


for v in arr:
    newV = reverse(v)

    if newV > 1 and isPrime(newV):
        print(newV, end=' ')
