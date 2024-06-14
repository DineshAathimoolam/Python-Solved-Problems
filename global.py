global n
n=1
print(n)


x=0
print(x)
def globe():
    global x
    x+=1
    return x
globe()
