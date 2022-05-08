"""
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
"""

a=0
b=1
n=4
sum=0

for i in range(0,n):
    print(a, end=' ')
    sum=a+b
    a=b
    b=sum
