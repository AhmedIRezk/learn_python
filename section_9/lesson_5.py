# get the user data
name = input('Enter your name: ').strip().lower()
company = input('Enter your company name: ').strip().lower()

birth = input('Enter your birth year: ')
email = input('Enter your email: ')

# get the index of the first space
spase_index = name.index(" ")
first_name = name[:spase_index]

# id = first 3 characters of company name + - + last 2characters of name + birth year
frist_3char_company = company[:3]
last_2char_name = name[-2:]
Id = frist_3char_company + '-' + last_2char_name + birth 

# email
index_at = email.index("@")
new_email = email[:index_at] + f"@{company}.com"
# greet the user
print('-'*50)
print(f"Hello, {first_name.title()}!\nwelcome at {company.title()}!")

# print the id and new email
print('-'*50)
print(f"Your id is: {Id}\nYour email is: {new_email}")