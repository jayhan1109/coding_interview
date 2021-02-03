import collections

N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))


def getMoney(arr):
    counter = collections.Counter(arr)
    if len(counter) == 1:
        return 10000+arr[0]*1000
    elif len(counter) == 2:
        return 1000 + counter.most_common(1)[0][0]*100
    else:
        arr.sort(reverse=True)
        return arr[0]*100


max = 0

for v in arr:
    money = getMoney(v)

    if money > max:
        max = money

print(max)
