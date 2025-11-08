# Calculate and classify BMI based on user's height and weight
# get height and weight
cm = float(input('Enter height in cm: '))
kg = float(input('Enter height in kg: '))
# getting height in meter for bmi
cm = cm/100
# calculating BMI
bmi = kg / (cm**2)
# check the BMI
if bmi >= 35:
    bmi_class = 'Extreme Obesity'
elif bmi>=30:
    bmi_class = 'Obesity'
elif bmi>=25:
    bmi_class = 'Overweight'
elif bmi>=18.5:
    bmi_class = 'Normal'
else:
    bmi_class = 'Underweight'

# print the result 
print('-'*20)
print(f'Yor BMI is {bmi:.2f} which is considered as {bmi_class}')





