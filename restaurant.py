import pandas as pd
menu={'FOOD ':['pizza','pretzel','salmon','cookies','chips','burger','croissant','shrimp','apple pie','crackers','checkin frise','lobster','cupcake','popcorn'],
'    TYPE OF FOOD':['Fast Food','Bread','Sea Food','Dessert','Snack','Fast Food','Bread','Sea Food','Dessert','Snack','Fast Food','Sea Food','Dessert','Snack'],
'     PRICE':['10$','3$','15$','5$','2$','7$','3$','20$','5$','2$','12$','25$','3$','5$']}
cart=[]
total=0
foods = ['pizza','pretzel','salmon','cookies','chips','burger','croissant','shrimp','apple pie','crackers','checkin frise','lobster','cupcake','popcorn']
print("  -------------------------------------------------")
print("               WELCOME TO OUR RESTURANT          ")
print("  ------------------------------------------------")
print("          -------------MENU-------------       ")
print() 

df = pd.DataFrame(menu)
print(df)

print()
print("-----------------------------")
while True:
	 order = input("Select an item (q to quit):").lower()
	 if order == "q":
	 	break
	 elif order in foods:
	 	cart.append(order)
	 else:
	 	print("Sorry your order dosenot exist in our menu !!")
indexes = [foods.index(i) for i in cart]
types = [menu['    TYPE OF FOOD'][i] for i in indexes]
prices = [menu['     PRICE'][i] for i in indexes]
for i in indexes:
	total += float(menu['     PRICE'][i].replace("$",""))
fi = {
'FOOD ':cart,
'    TYPE OF FOOD':types,
'     PRICE':prices
}

print("----------YOUR ORDER----------")
print()
do = pd.DataFrame(fi)
print(do)
print()
print(f"Total is: ${total:.2f}")