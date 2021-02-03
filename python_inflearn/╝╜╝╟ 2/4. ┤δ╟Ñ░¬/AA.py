N = int(input())
scores = list(map(float, input().split()))

avg, idx, minNum, val = 0, 0, float('inf'), 0

for score in scores:
    avg += score

avg = round(float(avg)/N)

for i, v in enumerate(scores):
    diff = abs(v-avg)

    if diff == minNum:
        if v == val or v < val:
            continue
        else:
            minNum = diff
            val = v
            idx = i

    elif diff > minNum:
        continue

    else:
        minNum = diff
        val = v
        idx = i


print(avg, idx+1)
