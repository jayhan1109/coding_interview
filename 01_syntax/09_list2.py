a = [23, 12, 36, 53, 19]

print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')

print()

for x in a:
    print(x, end=' ')

print()

for x in enumerate(a):
    print(x[1])

for i, v in enumerate(a):
    print(i, ":", v, sep='', end=' ')

print()

if all(45 > x for x in a):
    print("YES")
else:
    print("NO")

if any(15 > x for x in a):
    print("YES")
else:
    print("NO")
