N, K = map(int, input().split())
cards = list(map(int, input().split()))

res = set()

for p in range(N):
    for q in range(p+1, N):
        for m in range(q+1, N):
            res.add(cards[p] + cards[q] + cards[m])

res = list(res)
res.sort(reverse=True)
print(res[K-1])
