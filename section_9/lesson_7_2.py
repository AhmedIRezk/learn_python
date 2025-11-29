# get inputs from user
name = input("Enter your full name: ")
birth_date = (input("Enter your birth date (dd-mm-yyyy): "))
current_year = float(input("Enter your current year: "))

# get first name
first_name = name.split()[0]

# Calculator of age\
birth_year = birth_date.split("-")[-1]

age = int(current_year) - int(birth_year)

# greet user and print age
print("-"*40)
print(f"Hello, {first_name}\nWelcome at Age calculator")
print("-"*40)
print(f"Your age is: {age}")