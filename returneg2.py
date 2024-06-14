
def user_name():
    return(input("Enter your name: "))
def password():
    return(input("Enter your password: "))
a=user_name()
b=password()
print("Your name is :",a)
print("Your password is :",b)
if a=="Dinesh" and b=="Dinesh@6267":
    print("Your user name and password are correct you go ahead further process.")
else:
    if a !="Dinesh":
        print("Your user name is Wrong kindly check.")
    if b !="Dinesh@6267":
        print("You Entered wrong password kindly check")
print("Thank you")    
    
