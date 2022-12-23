a=int(input("inter your num1:"))
b=int(input("inter your num2:"))
if a>b:
    temp=a
    a=b
    b=temp
for i in range(a,b):
    print(i)
