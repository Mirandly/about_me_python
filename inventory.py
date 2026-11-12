inventory = {
    "laptop": {"price": 999.99, "quantity": 15}, 
    "mouse": {"price": 29.99, "quantity": 50},
    "keyboard": {"price": 39.99, "quantity": 45},
    "tablet": {"price": 249.99, "quantity": 30}
}
print("=" * 15 + " STORE INVENTORY " + "=" * 15)
print(f"\n{"Product":<20}{"Price":<20}Quantity")
print("-" * 55)
for product, info in inventory.items():
    print(f"{product:<20}${info["price"]:<22}{info["quantity"]}")

print(f"\n{"Products":<30} {"Total"}")
print("-" * 55)
total_value = 0
for product, info in inventory.items():
    total_value += info["price"] * info["quantity"]
    print(f"{product:<30}${total_value:.2f}")

search = input(f"\nLook up a product (enter product name): ").lower()
product_info = inventory.get(search)
if product_info:
    print(f"\nFound: {search}")
    print(f"Price: ${product_info["price"]:.2f}")
    print(f"Quantity: {product_info["quantity"]}")

else:
    print(f"No product found for '{search}'.")    

updated = input("Whould you like to update a product? ").lower()
if updated == "yes":
    search_product = input("Enter product you would like to update: ").lower()  
    operation = input("Is this sales or restock? ").lower()

    if operation == "sales":
         units = int(input("Enter the number of units sold: "))
         inventory[search_product]["quantity"] -= units
         print(f"Updated quantity: {inventory[search_product]["quantity"]}")

    elif operation == "restock":
         units = int(input("Enter the number of units restocked: "))
         inventory[search_product]["quantity"] += units
         print(f"Updated quantity: {inventory[search_product]["quantity"]}")

    for product, info in inventory.items():
         if info["quantity"] < 10:
          print(f"LOW STOCK ALERT: {product}")

elif updated == "no":
    pass          
    
    
     

    
