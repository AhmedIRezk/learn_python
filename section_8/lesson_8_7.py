# check if the string contain numbers, letters, both or also other characters

# # get the input
inp = input('Enter your input: ')
# check if contains numbers or alphabets using isalnum()
if inp.isalnum():
    # check if contains numbers only using isnumeric()
    if inp.isnumeric():
        print('you entered a num')
    # check if contains alphabets only using isalpha()
    elif inp.isalpha():
        print('you entered a letters')
        # check if the letters are all lower case using islower()
        if inp.islower():
            print('All letters are lowecase')
        # check if the letters are all upper case using isupper()
        elif inp.isupper():
            print('All letters are upprecase'.upper())
        # otherwise there is letters in both upper and lower case
        else:
            print('There is a mix between uppercase and lowercase letters')
    else:
        print('there is a mix between isnimeric and isalpha')
# otherwise there is other characters than numbers and letters
else:
    print('Your string did not contain alphabet and Numbers only!!')