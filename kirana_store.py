import pandas as pd

# Sample inventory data
inventory = {
    'Item': ['Rice', 'Wheat', 'Sugar', 'Milk', 'Oil'],
    'Stock': [50, 40, 30, 20, 10],
    'Price': [60, 45, 50, 30, 150]
}

# Creating DataFrame
store = pd.DataFrame(inventory)

# Function to display items
def display_items():
    print("\nAvailable Items:")
    print(store)

# Function to check stock availability
def check_stock(item, quantity):
    if item in store['Item'].values:
        index = store[store['Item'] == item].index[0]
        return store.loc[index, 'Stock'] >= quantity
    return False

# Function to purchase items
def purchase_item(item, quantity):
    if check_stock(item, quantity):
        index = store[store['Item'] == item].index[0]
        total_price = store.loc[index, 'Price'] * quantity
        store.loc[index, 'Stock'] -= quantity
        print(f"\nPurchase Successful! Item: {item}, Quantity: {quantity}, Total Price: ₹{total_price}")
    else:
        print("Purchase Failed! Insufficient stock.")

# Main menu function
def main():
    while True:
        print("\nKirana Store Management System")
        print("1. Display Items")
        print("2. Check Stock")
        print("3. Purchase Item")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_items()
        elif choice == '2':
            item = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            if check_stock(item, quantity):
                print("Stock is available!")
            else:
                print("Not enough stock available.")
        elif choice == '3':
            item = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            purchase_item(item, quantity)
        elif choice == '4':
            print("Thank you for using the Kirana Store Management System!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the application
if __name__ == "__main__":
    main()
