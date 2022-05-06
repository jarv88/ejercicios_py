
a=0
b=1
n=10
sum=0

for i in range(0,n):
    print(sum, end=' ')
    sum=a+b
    a=b
    b=sum
