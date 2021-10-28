n = int(input())
name = []
ethnic = []
for i in range(n):
    a, b = input().split()
    name.append(a)
    ethnic.append(b)
maxx = 0
flag = 0
for i in range(n):
    if ethnic.count(ethnic[i]) > maxx:
        maxx = ethnic.count(ethnic[i])
        flag = i
        #print(flag)
ans =""
for i in range(n):
    if ethnic[i] == ethnic[flag]:
        ans = ans + name[i] + " "
print(ans)

