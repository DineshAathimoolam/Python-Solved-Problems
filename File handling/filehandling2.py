d=open("C:/Dinesh/Demo12.txt","r+")
s=input("Enter the Keyword ")
count=0
for line in d.readlines():
    count+=1
    if s in line:
        print("Keyword found in line number ",count)
d.close()        
