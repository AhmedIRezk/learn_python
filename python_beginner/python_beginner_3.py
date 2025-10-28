# ask about number of hours
num_hours = float(input("enter number of hours: "))

# ask about rate
rate = float(input("enter hourly rate: "))
print('-'*20)

base_hours = 100
bonus = 2
# calculate salary
if num_hours > base_hours:
    over_hours = num_hours - base_hours
    salary = (base_hours * rate) + (over_hours * rate * bonus)
    
else:
    salary = num_hours * rate
# print the salary
print(f'you have worked {num_hours} hours this month, your salary is {salary:,.2f}$') 

