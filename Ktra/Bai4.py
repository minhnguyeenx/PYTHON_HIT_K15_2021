def tach(s: str):
    st = str()
    cnt = 1
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]: 
            cnt+=1
        else:
            st = st+str(cnt)+s[i]
            cnt = 1
    st = st + str(cnt) + s[len(s)-1]
    return st

ss = input()
s, n = ss.split(" ")
n = int(n)
for i in range(1, n+1):
    print(tach(s))
    s = tach(s)
