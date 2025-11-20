# Add employee bonus calculator based on employee ID and work details
# employees and their ids

juniors = ['1111', '1113', '1115', '1117',
'1119', '1121']
mid_level = ['1311', '1313', '1315', '1317',
'1319', '1321', '1323', '1325']
seniors = ['1519', '1521', '1523', '1525']

ID = input('Enter Employee id: ')
# get salary info
rate = float(input('Enter Hourly Rate: '))
hour = float(input('Enter Hours worked this month: '))
print('-'*20)

# calculate salary
salary = rate * hour
if ID in juniors:
    ponus = salary * 3
elif ID in mid_level:
    ponus = salary * 6
elif ID in seniors:
    ponus = salary * 9
else:
    ponus = 0
    print('Not an employee')

# print salary info
if ponus != 0:
    print(f'Employee id: {ID} gets a bonus of {ponus:,.2f} EGP')


