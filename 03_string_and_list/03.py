import sys
sys.stdin = open("03_string_and_list\input.txt", "rt")

N = 10
list = []

for i in range(20):
    list.append(i+1)

for r in range(N):
    a, b = map(int, input().split())

    p = a-1
    q = b-1

    while p < q:
        list[p], list[q] = list[q], list[p]
        p += 1
        q -= 1

for v in list:
    print(v, end=' ')
