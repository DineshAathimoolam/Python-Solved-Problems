s=set()
s.add(1)
s.add(2)
s.remove(1)
print(s)

print("-------------------------------------")

myNewset=set()
myNewset.add("I am Dinesh")
myNewset.add("from salem")
myNewset.add("Now I am Working in Cbe")

"I am Dinesh" in myNewset

myNewset.remove("from salem")

print(myNewset)

print("--------------------------------")

a={1,2,3,4,5,6}
b={1,2,3,8,4,6}
c=a.difference(b)
print(c)
d=b.difference(a)
print(d)
e=a-b
print(e)
f=b-a
print(f)
print("-------------------------------")
