f=open("C:/Dinesh/Demo12.txt","r+")
stud=[]
for line in f.readlines():
    value=line.split()
    stud.append([value[0],value[1],value[2]])
print(stud)
f.close()
    


k=open("C:/Dinesh/Demo12.txt","r+")
stu1=[]
for lines in k.readlines:
    val=lines.split()
    stu1.append([val[0]],[val[1]],[val[2]])

print(stu)
f.close()
