# get compare numbers
print('enter numbers you wont to compare:\n-------------- ')


# enter the numbers
num1 = float(input('enter the first number: '))
num2 = float(input('enter the sacond number: '))
num3 = float(input('enter the third number: '))
print ('-'*20)

# compare the numbers
if num1 > num2 :
    if num1 > num3:
        print(f'{num1} is the greatest number ')
    else :
        print(f'{num3} is the greatest number')  
else:
    if num2 > num3:
        print(f'{num2} is the greatest number ')  
    else:
        print(f'{num3} is the greatest number ') 


