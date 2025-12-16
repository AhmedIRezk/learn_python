import random
winer = random.randint(1,2)
num = int(input("Guess the coin flip!\nEnter\n1 for Heads\n2 for Tails\n"))

if winer == 1:
    print('the coin in Heads')
else:
    print('the coin in Tails')

print("-"*30)

if num == (winer):
    print ("you won")

else:
    print ("you lost")