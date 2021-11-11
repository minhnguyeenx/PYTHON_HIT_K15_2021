#kiểm tra xem xâu có nhiều hơn 10 kí tự hay không
def check(s: str)->bool:
    if len(s) >= 10: return True
    return False

s = input()
if check(s) == False: print(s)
else: print(s[0]+ str(len(s) -2 ) + s[len(s)-1])