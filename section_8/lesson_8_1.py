# Add grade evaluation program based on score input
score = float(input('enter ascore betwen 0 and 100: '))

if not ( 0<=  score <= 100):
    grate = None
    print('please enter a score betwen 0 and 100 ')
elif score >= 90:
    grate = 'A'
elif score >= 80:
    grate = 'B'
elif score >=70:
    grate = 'C'
elif score >= 60:
    grate = 'D'
else:
    grate = 'F'
if grate is not None :
    print(f'Your score is {score} and youe grate is {grate}')       


