str1=input("enter the string")
a = {}
for i in str1:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
print("Count of all characters in  :\n "+str(a))