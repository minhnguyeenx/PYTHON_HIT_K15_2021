def xd10(s: str) ->bool:
    '''
    :params:
    input: 
        số cần kiểm tra
    output:
        nếu trong số có số '1' hoặc '0'-> nó là số 10 thì return true
        không thì return false
    '''
    if '1' in s or '0' in s:
        return True
    return False

def ss10(s1: str, s2: str):
    '''
    :params:
    input:
        hai số cần so sánh
    output:
        nếu hai số đó có vị trí số '1',số '0' giống nhau, thì nó là 2 điểm 10
        tương tự nhau -> return true
        không thì -> return false
    '''
    set1 = set() #lưu vị trí i của số 1, số 0 của số đầu tiên
    set2 = set() #lưu vị trí i của số 1, số 0 của số thứ 2
    for i in range(len(s1)):
        if s1[i] == '1' or s1[i] == '0':
            set1.add(i)
    for i in range(len(s2)):
        if s2[i] == '1' or s2[i] == '0':
            set2.add(i)
    if set1 == set2: #vị trí giống nhau thì return true 
        return True
    return False     #không thì return false

a = list(map(str, input().split()))
cnt = 0 
L = [] #dãy chữa các số 10
for i in range(len(a)):
    if xd10(a[i]):
        L.append(a[i]) 
#print(L)

#đếm các số 10
for i in range(len(L) - 1):
    for j in range (i+1, len(L)):
        if L[i] != ' ' and ss10(L[i], L[j]):
            L[j] = ' ' #đổi giá trị của L[j] để tránh bị lặp lại
            cnt+=1 #đếm các số 10 giống L[i] với j > i
print(len(L)-cnt)
