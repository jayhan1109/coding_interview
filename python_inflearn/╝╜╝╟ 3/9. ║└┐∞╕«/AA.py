N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

arr.insert(0, [0]*(N+2))
arr.append([0]*(N+2))

for i in range(N):
    arr[i+1].append(0)
    arr[i+1].insert(0, 0)

for i in range(N):
    for j in range(N):
        if arr[i+1][j+1] > arr[i][j+1] and arr[i+1][j+1] > arr[i+1][j] and arr[i+1][j+1] > arr[i+1][j+2] and arr[i+1][j+1] > arr[i+2][j+1]:
            cnt += 1

print(cnt)
