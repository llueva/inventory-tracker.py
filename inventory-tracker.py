#variable for options

def display_options():
    options = "(1) View Inventory 2) Add Item (3) Drop Item (4) Exit "
    selected_option = int(input(options))
    return selected_option



#list (no user input)

inventory = ["power up", "gravity gun", "pistol", "master bow & arrow"]




#variables

def view_inventory():
    print("-------------------------------")
    print(f"{len(inventory)} items in inventory")
    print(inventory)
    print("-------------------------------")

    
def add_item():
    item = input("What item would you like to add to your inventory? ")
    inventory.append(item)
    print(f"{item} was successfully added to your inventory!")
    
def drop_item():
    view_inventory()
    index = int(input("Which item index number would you like to drop? "))
    dropped_item = inventory.pop(index) 
    print(f"{dropped_item} has been successfully removed!")

    
#looping through options
    
while True:
    selected_option = display_options()
    if selected_option == 1:
        view_inventory()
    elif selected_option == 2:
        add_item()
    elif selected_option == 3:
        drop_item()
    elif selected_option == 4:
        print("Goodbye!")
        break