import sys
sys.stdin = open("03_string_and_list\input.txt", "rt")

N, target = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
r = 0
sum = arr[0]
cnt = 0

while True:
    if sum < target:
        r += 1
        if r >= len(arr):
            break
        sum += arr[r]
    elif sum == target:
        cnt += 1
        if l == r:
            r += 1
            if r >= len(arr):
                break
            sum += arr[r]
        else:
            sum -= arr[l]
            l += 1
    else:
        sum -= arr[l]
        l += 1

print(cnt)
