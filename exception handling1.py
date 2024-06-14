class error(Exception):
    pass
class Toosmallerror(error):
    pass
class Toolargeerror(error):
    pass
num=int(input('Enter The number: '))
while True:
    try:
        ch=int(int(input('Enter The Number: ')))
        if ch<num:
            raise Toosmallerror
        elif ch>num:
            raise Toolargeerror
        break
    except Toosmallerror:
        print('You entered a Small Number,Try again')
    except Toolargeerror:
        print('You entered a Small Number,Try again')
print('You Entered Wrong Number')        
        

   
