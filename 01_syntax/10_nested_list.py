'''
b = []
for i in range(3):
    b.append([])
    for j in range(3):
        b[i].append(0)

print(b)
b[1][2] = 3
print(b)
'''

a = [0]*3
print(a)

a = [[0]*3 for _ in range(3)]
print(a)

a[0][1] = 5
print(a)

a[1][2] = 2
print(a)

for x in a:
    print(x)

for x in a:
    for y in x:
        print(y, end=' ')
    print()
