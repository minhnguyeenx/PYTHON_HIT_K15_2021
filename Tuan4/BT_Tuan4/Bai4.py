input()
L = list(map(int, input().split()))

#đếm số lần xuất hiện của từng phần tử trong dãy
for i in set(L):
    cnt = 0
    for j in L:
        if j == i:
            cnt+= 1
    print(i , ":", cnt)