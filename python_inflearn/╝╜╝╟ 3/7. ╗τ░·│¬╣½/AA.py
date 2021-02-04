N = int(input())
arr = []
total = 0

for i in range(N):
    arr.append(list(map(int, input().split())))

n = m = N//2

for i in range(N):
    for v in range(n, m+1):
        total += arr[i][v]

    if i < N//2:
        n -= 1
        m += 1
    else:
        n += 1
        m -= 1

print(total)
