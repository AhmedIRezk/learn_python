# getting the "number" of houres and "rate" 
num_hours = float(input('enter the number of hours per month: '))
rate = float(input("enter your hourly rate "))

# the basec hours
base_hours = 100
#the bonus
bonus = 2 

# check if the number of hours is greater than the base hours
if num_hours > base_hours :            
# calculate salary with bonus
    over_hours = num_hours-base_hours
    salary= (base_hours*rate)+(over_hours * rate * bonus)
else:
    # calculate normal salary
    salary=(base_hours*rate)
#print salary
print(f"you have worked {num_hours} hours this month,your salary is {salary:,.2f}")
