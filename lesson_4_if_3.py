# getting the total amount of money
mony = float(input('Enter the amount of mony you have: '))
print('-'*20)
# getting the price of the items
price1 = float(input('Enter the price of first item: '))
price2 = float(input('Enter the price of sacond item: '))
price3 = float(input('Enter the price of third item: '))
print('-'*20)
# calculate the total price
total_price = price1 + price2 + price3
diff_mony = mony - total_price

if  mony >= total_price  :
    print(f'Item have been purchased successfully\nthe remaining amount is: {diff_mony:.2f}$')
else:
     print('Sorry, You don\'t have enough balance')
     print(f'You need to add extra {diff_mony:.2f}$')
