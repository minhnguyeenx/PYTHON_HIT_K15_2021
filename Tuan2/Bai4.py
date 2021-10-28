L = list(map(int, input().split()))
k = int(input())
res = 0
for i in range(0, len(L)):
    res += L[i+1: ].count(k - L[i])
print(res)

