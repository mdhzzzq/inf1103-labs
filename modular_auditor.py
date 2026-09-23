inventory = 0
failed_entries = 0

# Continuously ask for stock quantity
while True:
    stock = input("Enter stock quantity (or type 'quit' to exit): ")

    # Check if the user wants to quit
    if stock.lower() == "quit":
        break

    # Check if the input is a valid integer
    if not stock.isdigit():
        print("Error: Please enter a valid positive integer.")
        failed_entries += 1
        continue

    # Convert the input from string to integer
    stock = int(stock)

    # Add the valid stock to the inventory
    inventory += stock

    print("Stock added successfully.")
    print("Current inventory:", inventory)

    # Check for overstock
    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break

# Final report
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)