import sys
sys.stdin = open("03_string_and_list\input.txt", "rt")

N = int(input())
idx = 0
isPalindrome = True

for i in range(N):
    idx += 1
    isPalindrome = True
    s = list(input().lower())

    p = 0
    q = len(s)-1

    while p < q:
        if s[p] != s[q]:
            print(f'#{idx} NO')
            isPalindrome = False
            break
        p += 1
        q -= 1

    if isPalindrome:
        print(f'#{idx} YES')
