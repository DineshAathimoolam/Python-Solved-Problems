f=open('C:/Python/area of circle.py','r+')
inp=input("Enter the keyword :")
count=0
for line in f.readlines():
    count+=1
    if inp in line:
        print("Keyword found in line number :",count)
f.close()        
