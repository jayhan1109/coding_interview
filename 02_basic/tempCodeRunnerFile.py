N = int(input())
cnt = 0

for v in range(2, N+1):
    for n in range(2, v):
        if v % n == 0:
            break
    else:
        cnt += 1

print(cnt)
