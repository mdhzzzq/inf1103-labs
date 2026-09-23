def get_valid_input():
    while True:
        stock = input("Enter stock quantity (or type 'quit' to exit): ")

        if stock.lower() == "quit":
            return "quit", False

        if not stock.isdigit():
            print("Error: Please enter a positive integer.")
            return None, True

        return int(stock), False


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):
    tax = amount * 0.10
    return tax



def generate_report(total_units, failed_attempts):
    print("\n--- Final Report ---")
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


inventory = 0
failed_attempts = 0
deliveries_processed = 0


while True:
    stock, failed = get_valid_input()

    if stock == "quit":
        break

    if failed:
        failed_attempts += 1
        continue

    inventory = process_delivery(inventory, stock)

    tax = calculate_tax(stock)

    deliveries_processed += 1

    print("Delivery added successfully.")
    print("Current inventory:", inventory)
    print("Tax for this delivery:", tax)



generate_report(deliveries_processed, failed_attempts)