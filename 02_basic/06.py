import sys
sys.stdin = open("02_basic\input.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
max = 0
ans = 0


def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


for v in arr:
    cur = digit_sum(v)

    if ans < cur:
        ans = cur
        max = v

print(max)
