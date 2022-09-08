#write a python script to calculate  sum of even first N natural number.
sum=0
i=1
a=21
while i<=a:
    if i%2==0:
        sum=sum+i
    i+=1
print("sum of even number =",sum) 

'''sum=0
a=21
for i in range(1,a):
    if i%2==0:
        sum=sum+i
print("sum of even natural number =", sum) '''   

