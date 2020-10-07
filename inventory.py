# *******************************
# * Author: Doug Smyka          *
# * Application: Inventory      *
# * Date Created: 10.6.2020     *
# * Date Revised: 10.7.2020     *
# *******************************

# Function for adding a new item to the inventory
def add_new_item(info):
    global inventory
    inventory[info[0]] = {'Quantity': info[1], 'Price': info[2], 'Description': info[3]}


# Function for getting information from user
def new_item():
    global itemList
    print('item: ', end='')
    v1 = input().lower()
    itemList.append(v1)
    print('Quantity: ', end='')
    v2 = input().lower()
    print('Price: ', end='')
    v3 = input().lower()
    print('Description: ', end='')
    v4 = input().lower()
    add_new_item([v1, v2, v3, v4])


# Function for asking user if they would like to add an item
def ask_user():
    add_item = True
    while add_item is True:
        print('Would you like to add an item? ', end='')
        user_response = input().lower()
        if user_response == 'yes' or user_response == 'y':
            new_item()
        else:
            add_item = False

# Function to search for an item
def item_search():
    global inventory
    print('Please enter the item you are searching for: ', end='')
    user_response = input().lower()
    if user_response in inventory:
        print('Quantity: %(Quantity)s Price: %(Price)s Description: %(Description)s' % (inventory[user_response]))
    else:
        print('Item not in inventory')


# Function to ask user if they want to search for an item
def ask_search():
    search = True
    while search is True:
        print('Would you like to search for an item in the inventory? ', end='')
        user_response = input().lower()
        if user_response == 'yes' or user_response == 'y':
            item_search()
        else:
            search = False


# Function for printing table
def print_table():
    global inventory
    global itemList
    j = 0
    print('\n*******************   Inventory   **********************\n')
    for i in inventory:
        item = itemList[j]
        j += 1
        print('[%s] ' % item, end='')
        print('Quantity: %(Quantity)s Price: %(Price)s Description: %(Description)s' % (inventory[i]))
    print('\n********************************************************\n')


# Function for main
def main():
    ask_user()
    ask_search()
    print_table()


# Initialization
inventory = {}
itemList = []

# Main
main()

# EOF
