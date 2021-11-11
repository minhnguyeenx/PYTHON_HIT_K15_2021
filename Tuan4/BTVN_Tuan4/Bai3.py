#cho các số đã sắp xếp vào xâu, thêm các phép +
def sx(L: list)->str:
    ans = str()
    for i in L:
        ans += str(i)+"+"
    return ans[:len(ans)-1]

#nhập list và sắp xếp list nhập vào
L = sorted(list(map(int, input().split("+"))))
print(sx(L))