# get name remove tralling spaces
name = input("enter ypur name: ").strip()

# replas spaces with underscore and make all letter small
# and  replase each 'a' with 'aaa'

username = name.replace(' ','_').lower().replace('a','aaa')

# add '@codzilla' to the end the user name
username = f'{username}@codzilla.com'
# greet user
print(f'hello {name.title()}')

# print username
print(f'your username is\n {username}')

