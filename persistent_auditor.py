import json

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            data = json.load(file)

        return data["total"], data["history"]

    except FileNotFoundError:
        return 0, []


inventory, transaction_history = load_inventory()

