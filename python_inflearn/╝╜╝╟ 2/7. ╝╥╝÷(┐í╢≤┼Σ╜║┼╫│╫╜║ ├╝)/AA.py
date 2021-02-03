N = int(input())
cnt = 0

nums = [False]*N

for i in range(2, N+1):
    if nums[i-1] == True:
        continue

    else:
        cnt += 1

        for v in range(i+i, N+1, i):
            if v % i == 0:
                nums[v-1] = True

print(cnt)
