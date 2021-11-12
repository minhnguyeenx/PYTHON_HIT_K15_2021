def check(num: int):
    cnt = 0
    for i in range(1,num+1):
        if num%i == 0:
            cnt += 1
    return True if cnt == 3 else False

n = int(input())
L = list(map(int, input().split(" ")))
ans = 0
for i in L:
    if check(i):
        ans += 1
print("Không" if ans == 0 else ans)