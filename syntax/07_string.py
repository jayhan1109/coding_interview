msg = "It is Time"
print(msg.upper())
print(msg.lower())
print(msg)

tmp = msg.upper()
print(tmp)
print(tmp.find('T'))
print(tmp.count('T'))

print(msg)
print(msg[:2])
print(msg[3:5])
print(len(msg))

for i in range(len(msg)):
    print(msg[i], end='')

print()

for i in msg:
    print(i, end='')

print()

for i, v in enumerate(msg):
    print(i, v, sep='', end=' ')

print()

for x in msg:
    if x.isupper():
        print(x, end=' ')

print()

for x in msg:
    if x.islower():
        print(x, end=' ')

print()

for x in msg:
    if x.isalpha():
        print(x, end='')

print()

for x in msg:
    if x.isalnum():
        print(x, end='')

print()

for x in msg:
    if x.isdigit():
        print(x, end='')

tmp = 'AZ'
for x in tmp:
    print(ord(x))

tmp = 65
print(chr(tmp))
