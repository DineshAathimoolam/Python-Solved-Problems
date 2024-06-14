salary=int(input('Enter your Salary: '))
age=int(input('Enter your Age: '))
if (salary>=20000) and (age<=25 and age>=18):
    required_loan=int(input('Enter your required Loan Amount: '))
    if required_loan <=100000:
        print(required_loan,",You are eligible for your required loan..")
    else:
        print('Your required Loan amount is Higher....!')
else:
    print("You are not eligible for your required loan..")
