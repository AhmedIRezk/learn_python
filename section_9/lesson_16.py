# Add simple random winner checker using randint and list membership

import random
winer_1 = random.randint(1,20)
winer_2 = random.randint(1,20)
winer_3 = random.randint(1,20)
winer_4 = random.randint(1,20)

winerse = [winer_1 , winer_2 , winer_3 , winer_4 ]

num = int(input("Enter the number between 0 and 20\n"))
print("-"*20)
print(winerse)
if num in winerse :
    print("you win...")
else:
    print("you lost !!")




