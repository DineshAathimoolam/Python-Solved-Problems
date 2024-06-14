count=0
count1=0
a=int(input("Enter the starting point "))
b=int(input("Enter the Ending point "))
for i in range(a,b+1):
    if i%2==0:
        print(i)
        count=count+1
        
    if i%2!=0:
        print(i)
        count1=count1+1
    
print("The  Even no count is :",count)
print("The  ODdd no count is :",count1)

