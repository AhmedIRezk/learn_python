# //////////////////////////////////////////////// test lesson 8 !!!!
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

# ////////////////////////////////// progect "1" ...

# geeting
winners = ['mohamed', 'ahmed', 'mahmoud', 'islam','hassan','israa', 'mariam']
Name = input('Enter the wining name: ').lower()

if Name in winners :
    print(f'congratulation {Name} is a winner !!!')
else :
    print(f'sorry {Name} is not a winner!')

# /////////////////////////////////// progect "2" ...

# data
Name_islam = 'islam_hesham@codezilla.com'
pass_islam = 'islam_codezilla'
Name_mohamed = 'mohamed_gouda@codezilla.com'
pass_mohamed = 'gouda_codezilla'

# input data
username = input('Enter username: ') 
password = input('Enter password: ')

# check if the username and password are correct
if (username == Name_islam and password == pass_islam) or (username == Name_mohamed and password == pass_mohamed ):
    print('Access is allowed')
else:
    print('sorry, access is not allowed')


# ///////////////////////////////////////////// progect "3"

# get the country name
contry = input("Enter contry name: ").lower()
# lists of countries and their weekends
countries_fri_sat = ['egypt', 'saudi arabia', 'ksa', 'kuwait']
countris_sat_sun = ['australia', 'usa', 'united states',
'united kingdom', 'uk']

if contry in countries_fri_sat:
    print(f'friday and sunday are the weekends in {contry.title()}')
elif contry in countris_sat_sun:
    print(f'saturday and sunday are the weekend in {contry.title()}')
else :
    print('sorry, I don\'t know')