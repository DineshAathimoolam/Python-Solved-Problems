d=open("C:/Python/avg.py","r")
str=d.readlines()
print(str)
d.close()
#iteration
a=open("C:/Python/avg.py","r")
total=len(a.readline())
print(total)
a.close()


b=open("C:/Python/avg.py","r")
for line in b:
    print("Hello")
    print(line)
    
b.close()
