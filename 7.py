str=input("enter the string")
print(str)
a=str[0]
str=str.replace(a,'$')
str=a[0]+str[1:]
print(str)
