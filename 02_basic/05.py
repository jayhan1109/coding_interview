import sys
import collections
sys.stdin = open("02_basic\input.txt", "rt")

N, M = map(int, input().split())

arr = []

for p in range(1, N+1):
    for q in range(1, M+1):
        arr.append(p+q)

counter = collections.Counter(arr)

max = counter.most_common(1)[0][1]

for i, v in counter.items():
    if max == v:
        print(i, end=' ')
