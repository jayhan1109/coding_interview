import sys
sys.stdin = open("03_string_and_list\input.txt", "rt")

N = input()
arr1 = list(map(int, input().split()))
M = input()
arr2 = list(map(int, input().split()))

list = arr1+arr2

list.sort()

for v in list:
    print(v, end=' ')
