f=open('C:/Dinesh/Demo12.txt','r+')
student=[]
for line in f.readlines():
    value=line.split()
    student.append([value[0],value[1],value[2]])
print(student)
f.close()
