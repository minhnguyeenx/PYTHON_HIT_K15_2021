L = list(map(int, input().split()))
result = []
sum = 0
for x in L:
    sum = sum + x
    result.append(sum)
print(result)