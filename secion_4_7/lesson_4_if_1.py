
num1 = float(input('enter a number: '))
num2 = float(input('enter the number to divide by: '))

result = num1 / num2 
print('-'*20)
print(f'the division result is {result}')

if num1 %3 == 0:
    print(f'{num1} is divisable by 3.0')
else:
    print(f'{num1} is not divisable by 3.0')
