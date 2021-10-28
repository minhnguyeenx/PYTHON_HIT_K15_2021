a = "TRẺTRÂU"
s = input()
i = 0
for word in s:
    if word == a[i]:
        #print(word)
        i+=1
        if(i >= 7) :break
if i == 7: 
    print("TRẺ TRÂU")
else: 
    print("Không TRẺ TRÂU")

