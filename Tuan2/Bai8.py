s = input()
cnt = s.count("1")
if cnt % 2 == 1:
    print("NO")
else:
    d = 0
    for i in range(len(s)):
        if s[i] == "1":
            d += 1
            if d == cnt/2 :
                print(s[:i+1], s[i+1:])
                break
