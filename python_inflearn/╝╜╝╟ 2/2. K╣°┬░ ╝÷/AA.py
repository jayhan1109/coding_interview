T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print(f'#{i+1} {sorted(arr[s-1:e])[k-1]}')
