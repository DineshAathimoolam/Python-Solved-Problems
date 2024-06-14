def outer_function():
    a=5
    def inner_function():
        nonlocal a
        a=10
        print("inner function:",a)
    inner_function()
    print("outer_function:",a)
outer_function()   
    
