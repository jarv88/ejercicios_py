
a=0
b=1
n=5
sum=0

for i in range(0,n):
    print(a, end=' ')
    sum=a+b
    a=b
    b=sum
