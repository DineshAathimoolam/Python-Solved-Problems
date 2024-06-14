import math
#log
a=int(input("Enter the 1st value: "))
b=int(input("Enter the 2nd value: "))
c=int(input("Enter the 3rd value: "))

res=math.log(a)+math.log(b)
res1=math.log(c)-math.log(b)
res2=math.log(c)/math.log(a)
res3=math.log(c)*math.log(a)

print(f"The result of log {a} + The result of log {b} is {res}")
print(f"The result of log {b} - The result of log {c} is {res1}")
print(f"The result of log {b} / The result of log {c} is {res1}")
print(f"The result of log {c} * The result of log {a} is {res1}")

#log10
num=int(input('Enter the Number: '))
log_10=math.log10(num)
print((f'The Logarith of base 10 of {num} is :{log_10}'))
