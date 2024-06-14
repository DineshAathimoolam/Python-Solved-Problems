#1
Read=open("C:/Dinesh/Demo123.txt","r")
str=Read.read()
print(str)
Read.close()

#2
lcm=open("C:/Dinesh/Demo123.txt","r")
print(lcm.read())
lcm.close()

#3
with open("C:/Dinesh/Demo123.txt","r") as file:
    data=file.read()
print(data)

#4
txt=open("C:/Dinesh/Demo123.txt","r")
txtRead=txt.read()
print(txtRead)
print('This is ',txt.read())
txt.close()

#5
lines=[]
with open("C:/Dinesh/Demo123.txt","r") as file:
    lines=file.readlines()

count=0
for line in lines:
    count+=1
    print(f'line{count}:{line}')
