# Question 1 -  Inventory System

# Creating a nested dictionary for inventory
inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}

# Customer's cart
cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}


def process_order(inventory, cart):
    grand_total = 0      # Stores total bill amount
    bill_items = []      # Stores purchased items which is later used in printing the bills

    # Process each item in the cart
    #eg: ("rice",2)__ ("milk",3)
    for item, quantity in cart.items(): # eg: first loop items = rice
                                        #quantity = 2 -- # eg: second loop items = milk
                                        #quantity = 3

        # Check if item exists in inventory eg rice in inventory
        if item in inventory:

            available_stock = inventory[item]["stock"] #eg: rice 20 

            # Check if enough stock
            if available_stock >= quantity: #20-2= 18

                price = inventory[item]["price"] #eg: rice 120 
                item_total = price * quantity    #240

                # Add item cost to grand total
                grand_total += item_total

                # Store bill information
                bill_items.append((item, quantity, item_total))

                # Update stock after purchase
                inventory[item]["stock"] -= quantity # rice: 20 - 3 = 17, later it is upade to inventory

            else:
                print(f"Sorry, not enough stock for {item}")

        else:
            print(f"{item} is not available in inventory")

    # Print bill
    print("\n------- BILL -------")

    for item, quantity, total in bill_items:
        print(f"{item} x {quantity} = NPR {total}")

    print("--------------------")
    print(f"Grand Total: NPR {grand_total}")
    print("--------------------")

    # Print updated inventory
    print("\nUpdated Stocks:")

    for item, details in inventory.items():
        print(f"{item} = {details['stock']}")


# Call the function
process_order(inventory, cart)