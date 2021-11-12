def sum(num: int):
    sum = 0
    for i in range(1, num):
        if num%i == 0:
            sum+=i
    return sum 

n = int(input())
L = sorted(set(list(map(int, input().split(" ")))))
lst =[]
for i in L:
    if sum(i) > i:
        lst.append(i)
print(len(lst))
print(*lst, sep = " ")
