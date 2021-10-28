num = int(input())
while num > 9:
    num = sum(map(int, str(num)))
print(num)