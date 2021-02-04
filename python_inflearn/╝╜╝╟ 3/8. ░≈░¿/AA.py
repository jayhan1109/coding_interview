N = int(input())
arr = []
sum = 0

for i in range(N):
    arr.append(list(map(int, input().split())))

M = int(input())

for i in range(M):
    a, b, c = list(map(int, input().split()))

    for j in range(c):
        if b == 0:
            arr[a-1].append(arr[a-1].pop(0))
        else:
            arr[a-1].insert(0, arr[a-1].pop())

n = 0
m = N

for i in range(N):
    for v in range(n, m):
        sum += arr[i][v]

    if i < N//2:
        n += 1
        m -= 1
    else:
        n -= 1
        m += 1

print(sum)
