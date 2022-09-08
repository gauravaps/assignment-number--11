'''a=121
sum=0
while a>0:
    remain=a%10
    sum=sum+remain
    a=a//10
print(sum) '''


n=int(input("enter the number"))
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print(sum)    