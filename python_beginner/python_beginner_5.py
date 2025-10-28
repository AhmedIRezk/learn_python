# ask your name
name = input('name: ').strip().title()

# ask your currency
currency = input('currency: ').strip().title()

# ask your number of hours
hour = input('number of hours: ')

# ask your hourly rate
rate = input('hourly rate: ')

# calculate salary
salary = float(hour) * float(rate)

# print salary
print('-'*20)
print(f' The Salary Of {name} is {salary} {currency} ') 