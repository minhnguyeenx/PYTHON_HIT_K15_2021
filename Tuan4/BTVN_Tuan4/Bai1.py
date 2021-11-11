s = input()
x = s[s.index("(")+1: s.index(",")]
y = s[s.index(",")+1: len(s)-1]
print(x, y)