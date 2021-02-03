n, k = map(int, input().split())

count = 0

for x in range(1, n+1):
    if n % x == 0:
        count += 1

        if count == k:
            print(x)
            break

else:
    print(-1)
