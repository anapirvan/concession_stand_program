menu = {"pizza": 3.76,
        "nachos": 4.80,
        "fries": 3.70,
        "soda": 3.00,
        "popcorn": 5.87}

cart = []
total = 0

print("--------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-------------------------")

while True:
    food = input("Select your order (q to quit): ").lower()
    if food == 'q':
        break
    if menu.get(food) != None:
        cart.append(food)

print("------- YOUR ORDER ------")

for food in cart:
    total += menu[food]
    print(food, end=" ")

print()
print(f"Your total is ${total:.2f}")
