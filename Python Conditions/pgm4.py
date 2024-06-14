mark_1=int(input('Enter your Tamil Mark :'))
mark_2=int(input('Enter your English Mark :'))
mark_3=int(input('Enter your Maths Mark :'))
mark_4=int(input('Enter your Science Mark :'))
mark_5=int(input('Enter your Social Mark :'))

Total=(mark_1+mark_2+mark_3+mark_4+mark_5)
Average=Total/5
if Average<35:
    print('Additional class is required..')
else:
    print('You are good to Go..')
    
