item = input("What item would you like to buy? ");
price = float(input("What is the price?: "));
quantity = int(input("How many would you like?: "));
total = price * quantity;

print(f"you have bougth {quantity} x  {item} for price  ${price} each");
print(f"total: ${total}");