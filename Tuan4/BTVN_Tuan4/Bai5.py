#đếm các xâu con(s[i:j]) có trong xâu s
def cnt(s: str):
    ans = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s.count(s[i:j]) >= 2:
                ans = max(ans, j-i+1)
    return ans

s = input()
print(cnt(s))