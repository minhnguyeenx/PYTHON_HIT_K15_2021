s = input().split(" ")
ans = 0
for i in range(len(s[1])):
    if s[1][i:i+len(s[0])] == s[0]:
        ans += 1
print(ans)