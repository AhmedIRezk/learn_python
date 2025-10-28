# ask your name
name = input('enter your name: ').strip().lower()

# get date of birth
year = input('enter your birth year ')
month = input('enter your birth month ')
day = input('enter your birth day ')
# replace space with underscore
username = name.replace(" ", "_")

# username = {username}_{day}_{month}_{int(year) + len(name)} @codzilla.com
username = f'{username}_{day}_{month}_{int(year) + len(name)}'
username = f'{username}@codzilla.com'
# geete the user
print("-"*20)
print(f'Hello {name.title()}') 
# print username
print(f'your username is ...\n{username}')
