def check(s1: set,s2: set) -> bool:
    '''
    :param:
    input:
        2 set đầu vào
    output:
        s1 là con của s2 ->true
        s1 không là con của s2 ->flase
    '''
    if len(s1-s2) == 0:
        return True
    return False

s1 = set(map(str, input().split()))
s2 = set(map(str, input().split()))
if check(s1, s2) :
    print('s1 là con của s2')
else: 
    print('s1 không là con của s2')
    