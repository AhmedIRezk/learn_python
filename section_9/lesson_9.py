# list of available vegetables
vegetables = ['broccoli', 'eggplant', 'carrot', 'cabbage', 
'cucumber', 'potato', 'garlic', 'pepper']

print('Welcome at Codezilla Vegetables!')
vegetabl = input("Enter the vegetable you want to get: ")
amount = input("Enter the amount in kg: ")

vegetables_join = ", ".join(vegetables[:-1])

if vegetabl.lower() in vegetables:
    print(f"we will get you {amount} kg of {vegetabl} very soon.")
else:
    print(f"sorry, we only have {vegetables_join} and {vegetables[-1]}")