import sys
sys.stdin = open("03_string_and_list\input.txt", "rt")

N = int(input())
arr = []
max = 0
tmp1 = 0
tmp2 = 0

for i in range(N):
    arr.append(list(map(int, input().split())))

for n in range(N):
    for m in range(N):
        tmp1 += arr[n][m]
        tmp2 += arr[m][n]

    if tmp1 > max:
        max = tmp1

    if tmp2 > max:
        max = tmp2

    tmp1 = 0
    tmp2 = 0


tmp1 = 0
tmp2 = 0

for i in range(N):
    tmp1 += arr[i][i]
    tmp2 += arr[i][N-i-1]

if tmp1 > max:
    max = tmp1

if tmp2 > max:
    max = tmp2

print(max)
