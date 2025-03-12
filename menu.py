menu = {
    'pizza': 110,
    'pasta': 70,
    'burger': 60,
    'coke': 45,
    'salad': 80
}

print("Welcome to the Restaurant!")
print("Menu Card:")
for item, price in menu.items():
    print(f"{item.capitalize()} : Rs{price}")

order_total = 0
chances = 5  # Maximum chances

for i in range(chances):
    item = input("Enter the name of the item you want to order: ").strip().lower()

    if item in menu:
        order_total += menu[item]
        print(f"{item.capitalize()} has been added to your order. Total so far: Rs{order_total}")
    else:
        print(f"Sorry, {item} is not available.")

    another_order = input("Do you want to order something else? (yes/no): ").strip().lower()
    if another_order == "no":
        break  # Exit if the customer says no

print(f"\nYour final bill amount is: Rs{order_total}")
print("Thank you for visiting our restaurant!")
