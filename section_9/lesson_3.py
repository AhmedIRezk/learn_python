# Add drink ordering system with categorized menus (hot drinks, soda, juices) and dynamic user selection flow
# a list of hot drinks, soda, and juices
drinks = [
# hot drinks
['Tea', 'Herbs', 'Hot Cider', 'Coffee', 'Hot Chocolate'],
# soda
['Coke', 'Pepsi', 'Fanta', 'Sprite', 'Mirinda'],
# juices
['Lemonade', 'Orange Juice', 'Mango Juice',
'Strawberry Juice', 'Apple Juice']
]

# a message to ask for the type of the drink
message_type_drink = f"""please, Enter the type of the drink you want to order:
1. Hot Drinks
2. Soda
3. Joices \n"""
# get the type of the drink index
order_index_type = int(input (message_type_drink))

# a message to ask the user for the drink
message_drink = f"""Please Enter the number of the drink want to order: 
1. {drinks[order_index_type -1][0]}
2. {drinks[order_index_type -1][1]}
3. {drinks[order_index_type -1][2]}
4. {drinks[order_index_type -1][3]}
5. {drinks[order_index_type -1][4]}
"""
# get the drink index
order_index = int(input(message_drink))
print('-'*50) 

# get the drink, choose the type then the drink
order = drinks [order_index_type -1][order_index -1]


# print the order
print('thanks for chooising codezillas cafe!')
print(f'please, Enjoy your time\nwhile we get {order} ready for you') 



