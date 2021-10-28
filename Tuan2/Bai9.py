L = list(map(lambda x: int(x[1]), input().split(",")))
#print(L)
even = []
odd = []
for x in L:
    even.append(x) if x % 2 == 0 else odd.append(x)
print(tuple(even + odd))