arr = [list(map(int, input().split())) for _ in range(9)]

print(arr)

isSudo = True

for i in range(9):
    if len(set(arr[i])) != 9:
        print("NO")
        isSudo = False
        break

tmp = set()

if isSudo:
    for i in range(9):
        for j in range(9):
            tmp.add(arr[j][i])

        if len(tmp) != 9:
            isSudo = False
            print("NO")
            break
        else:
            tmp = set()

tmp = set()

if isSudo:
    for i in range(3):
        for j in range(3):
            for m in range(3):
                tmp.add(arr[3*i+j][3*i+m])

        if len(tmp) != 9:
            print("NO")
            isSudo = False
            break

if isSudo:
    print("YES")
