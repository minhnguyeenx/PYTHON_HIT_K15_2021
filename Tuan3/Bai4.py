A = {'An', 'Binh', 'Nam', 'Long', 'Ngoc', 'Tu'}
B = {'Binh', 'Linh', 'Nam', 'Hai', 'Long'}
# a.Loại “Tu” ra khỏi danh sách
A.remove('Tu')
print(A)
# b.Thêm “Cuong” vào tập A
A.add('Cuong')
print(A)
# c.Tạo tập C chứa tất cả thành viên của tập A và tập B sao cho không trùng nhau
C = A|B
print(C)
# d.Tạo tập D chứa những thành viên thuộc tập A và B
D = A&B
print(D)
# e.Tạo tập E chứa những thành viên thuộc tập A nhưng không thuộc tập B
E = A-B
print(E)
# f.Tạo tập F chứa những thành viên chỉ nằm trong tập A hoặc tập B
F = A^B
print(F)