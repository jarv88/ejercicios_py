
a=0
b=1
n=4
sum=0
print(a,b, end=' ')
for i in range(0,n):
    sum=a+b
    a=b
    b=sum
    print(b, end=' ')
