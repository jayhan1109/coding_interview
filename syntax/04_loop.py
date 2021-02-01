'''
a = range(10)
print(list(a))

a = range(1, 11)
print(list(a))

for i in range(10):
    print(i)
    
i = 1
while i < 10:
    print(i)
    i += 1
    
for i in range(10, 0, -2):
    print(i)
    
i = 10
while i > 0:
    print(i)
    i -= 2

'''

for i in range(1, 11):
    print(i)
    if i > 15:
        break
else:
    print(11)
