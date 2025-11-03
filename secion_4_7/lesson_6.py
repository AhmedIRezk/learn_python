# greating
print('It is the time to see hieght differently 😃')
# getting the hieght
height = float(input('Enter the hieght in cm: ')) 
print('-'*20)
# compare the hieght        
if height >= 200:
    tall_class = 'very tall'
elif 180 <= height < 200:
    tall_class = 'tall'
elif 160 <= height < 180:
    tall_class = 'normal'
elif 150 <= height < 160:
    tall_class = 'short'
else:
    tall_class = 'very short'  
# print the height      
print(f'{height} cm is considered {tall_class}')   

# /////////////////////////////

print('It is the time to see if we could do better 😃')
print('-'*25)

num = float(input('enter the number: '))
guess = input(f'{num} is even or odd ??\n').lower()

if (num%2 == 0 and guess =='even') or (num%2 !=0 and guess =='odd'):
    print('Bravoooo!!! 🥳🥳')
else:
    print("No problem, let's try again 😀")


