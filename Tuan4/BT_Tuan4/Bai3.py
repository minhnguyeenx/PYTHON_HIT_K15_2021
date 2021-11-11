L = list(map(int, input().split()))

#list arr lưu trữ chỉ số của số lẻ trong dãy
ans = []
for i in range(len(L)):
    if L[i] % 2 == 1:
        ans.append(i)
#list new_list lưu trữ số chẵn trong dãy
new_list = list(filter(lambda x: (x%2 == 0), L))
print(*ans, sep = " ")
print(list(new_list))