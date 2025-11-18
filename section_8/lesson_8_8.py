# Add basic calculator script with user input and operation handling
# getting inputs
frist_num = float(input('Enter the frist num: '))
sacond_num = float(input('Enter the second num: '))
operation = input('Enter the operation: ')
# check the operator and do the operation
if operation == '+':
    operation_name = 'Addition'
    result = frist_num + sacond_num
elif operation == '-':
    operation_name = 'Subtraction' 
    result = frist_num - sacond_num
elif operation == '*':
    operation_name = 'Multiplication'
    result = frist_num * sacond_num
elif operation == '/':
    operation_name = 'Division'
    result = frist_num / sacond_num
elif operation == '**':
    operation_name = 'Power'
    result = frist_num ** sacond_num
else :
    operation = None
    print('sorry, please enter valid inputs')
# print the result
if operation !=None:
    print(f'{operation_name} result is {result}')



