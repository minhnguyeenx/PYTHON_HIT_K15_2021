#nhập list
def input_list():
    return list(map(int, input().split())) 
#nhập số nguyên
def input_int():
    return int(input()) 
#xóa số x đầu tiên trong dãy
def delete_x(L: list, x:int): 
    if x not in L:
        print("x not in L")
        return L, -1
    else:
        i = L.index(x)
        L.remove(L[i])
        return L, i
#xóa tất cả số x trong dãy
def delete_all_x(L: list, x: int):
    if x not in L:
        print("x not in L")
        return L
    else:
        while x in L:
            L.remove(L[L.index(x)]) 
        return L
#check xem vị trí y có thỏa mãn hay không
def check(L: list,y: int) -> bool:
    return y >= 0 and y < len(L)
#thêm số x vào vị trí y trong list
def insert_x(L: list, x: int, y: int)->list:
    if check(L, y) == False:
        print("Y is invalid")
        return L
    else:
        return L[:y]+[x]+L[y:]

L = input_list()
x = input_int()
#a
arr, id = delete_x(L, x)
print(L)
if id != -1: print(id)
#b
print(delete_all_x(L, x))
#c
y = input_int()
print(insert_x(L, x, y))


