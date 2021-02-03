arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')

for x in arr:
    if arrMin > x:
        arrMin = x

print(arrMin)
