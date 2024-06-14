import sys
a=[2,4,5,'a',8,6,0]
for i in a:
    try:
        c=2/i
        print(c)
    except:
        print('oops',sys.exc_info()[0],'Occured')

        
