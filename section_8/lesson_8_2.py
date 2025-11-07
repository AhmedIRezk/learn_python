# Add simple login authentication system
# data:
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