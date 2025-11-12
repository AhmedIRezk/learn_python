# Calculate final item price after applying discount based on item code

item_cod =(input('Enter the code item: '))
price =float(input('Enter the price: '))

sales_70 = ['070', '170', '270', '370', '470']
sales_50 = ['050', '150', '250', '350', '450']
sales_30 = ['030', '130', '230', '330', '430']

if item_cod in sales_70:
    sales = 0.70
elif item_cod in sales_50:
    sales = 0.50
elif item_cod in sales_30:
    sales = 0.30
else:
    sales = 0
# price = price * (1-sales)
price *=(1-sales)

print(f'the final price the item code-{item_cod} after {sales*100}% is {price:,.2f} EGP')

