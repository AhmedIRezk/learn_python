# Employees and their offices
cairo = ['Islam Mahfouz', 'Mohamed Mesilhy', 'Hatem Elmaghraby', 'Kareem Embaby']
riyadh = ['Mohamed Gouda', 'Ayman Hamed', 'Seif Ali', 'Adham Wael']
casablanca = ['Ahmed Ashraf', 'Abd El-Rahman Mahrous', 'Islam Sheta', 'Mohamed Medhat', 'Mahmoud Nasser']
dubai= ['Ahmed Alaa', 'Kareem Abd-Elmeged', 'Osama Ashraf', 'Mohamed Mostafa', 'Ahmed Bedeir']


# get office name
office = input('The name of the office: ').lower()

match office:
    case 'cairo' | 'egypt':
        employees = cairo
    case 'riyady'| 'saudi':
        employees = 'riyady'
    case 'casablanca' |'morocco':
        employees = casablanca
    case 'dubai' | 'uae':
        employees = dubai
    case _:
        employees = False
        print('not found')

# check if the office is found
if employees :
    employees_str = ', '.join(employees[:-1])
    
    print(f'The employees in {office.upper()} are: {employees_str} and {employees[-1]}')