# greeting
print("it is the time to see if we could do better")
print("-"*25)
# getting the numbers
first_num = float(input("Enter the number: ")) 
div_num = float(input("Enter the number to divide py: ")) 
guess = input(f"{first_num} is divisible by: {div_num} yes or no?\n").lower()

# compare the numbers and the guess
if (first_num % div_num==0 and guess=='yes') or (first_num % div_num!=0 and guess=='no'):
    print('-'*25)
    print('pravooooo!!!')
else: 
    print("no proplem, it's try again")
