N = int(input())
scores = list(map(int, input().split()))

total = 0
prev = 0

for v in scores:
    if v == 1:
        prev += 1
        total += prev
    else:
        prev = 0

print(total)
