try:
    print("I'll try to Print the Line of the Code")
except:
    print("I'll try to Print the Line of the Code if an error is Encountered")
print("-----------------------------------------------------------")    
class error(Exception):
    pass
class Error(error):
    pass

def sqrt(x):
    if x<0:
        raise Error('Exception Message')
    try:
        return x ** 0.5
    except Error:
        print('Exception message')
print("-----------------------------------------------------------")    
#integer form or not
try:
    Age=int(input('Enter your Age :'))
except:
    print('Age is Not Integer Form')

print("-----------------------------------------------------------")    
#what type of error
try:
    print (v)
except SyntaxError:
    print('There is Syntax Error Occured in your Code')
except NameError:
    print('There is Name Error Occured in your Code')
except TypeError:
    print('There is Type Error Occured in your Code')

print("-----------------------------------------------------------")    
def divide (x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print('Division by Error')
    else:
        print('Result is ',result)

divide(10,5)

print("-----------------------------------------------------------")    
num=input('Enter the Number :')
try:
    user_name=int(num)
    print('You have Entered the Number is :',user_name)
except:
    print('You have Entered a Wrong Number')

print("-----------------------------------------------------------")    
import sys
try:
    dinesh=('C:/Dinesh/Demo123')
    d=dinesh.readlines()
    i=int(s.strip())
except OSError as Err:
    print('os Error:{0}'.format(Err))
except ValueError:
    print('Could not Convert Data to an Integer ')
except:
    print('Unexpected Error',sys.exc_info()[0])
    #raise
    
































    
