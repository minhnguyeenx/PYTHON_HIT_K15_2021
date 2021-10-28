S1 = input("Nhập chuỗi 1: ")
while(len(S1) < 10):
    S1 = input("Nhập lại: ")
print("Độ dài chuỗi vừa nhập: ", len(S1))
print("Vt thứ 2 đến vt thứ 6 trong chuỗi: ", S1[1:6])

S2 = input("Nhập chuỗi 2: ")
print("Chữ hoa: ", S2.upper())
print("Chữ thường: ", S2.lower())
print("Thay kt b thành kt g: ", S2.replace("b", "g"))

S3 = "hElLo-mY-NAMe-iS-SuZIe"
S4 = S3.split("-")
S3 = " ".join([word.lower().title() for word in S4])
print(S3)