# Add student grade calculator with score validation
print('please enter scores between 0 and 100')
print('-'*20)

# get the scores
arabic = float(input('Enter Arabic scor: ')) 
english = float(input('Enter English scor: ')) 
math = float(input('Enter math scor: ')) 
physics = float(input('Enter physics scor: ')) 
chemistry = float(input('Enter chemistry scor: ')) 
biology = float(input('Enter biology scor: ')) 
print('-'*20)
# getting total score 
score = (arabic+ english+ math+ physics+ chemistry+ biology)/6

# getting the grade
if not(0 <=score<=100):
    grade = None
    print('please, enter a score between 0 and 100')
elif score>=90:
    grade='A'
elif score>=75:
    grade='B'
elif score>=60:
    grade='C'
elif score>=50:
    grade='D'
else:
    grade='F'

# print the result
if grade is not None:
    print(f'Youre score is {score:.2f}%\nYour grade is {grade}')


