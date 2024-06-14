lines=[]
with open("C:/Dinesh/Demo123.txt","r") as file:
    lines=file.readlines()

count=0
for line in lines:
    count+=1
    print(f'line{count}:{line}')
