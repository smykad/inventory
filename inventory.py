# *******************************
# * Author: Doug Smyka          *
# * Application: Inventory      *
# * Date Created: 10.6.2020     *
# * Date Revised: 10.6.2020     *
# *******************************

# Function for adding a new item to the inventory
def addNewItem(info):
    global inventory
    inventory[info[0]] = {'Quantity': info[1], 'Price': info[2], 'Description': info[3]}

# Function for getting information from user
def newItem():
    print('item: ', end='')
    v1 = input().lower()
    print('Quantity: ', end='')
    v2 = input().lower()
    print('Price: ', end='')
    v3 = input().lower()
    print('Description: ', end='')
    v4 = input().lower()
    addNewItem([v1, v2, v3, v4 ])

# Function for asking user if they would like to add an item
def askUser():
    addItem = True
    while addItem is True:
        print('Would you like to add an item? ', end='')
        userResponse = input().lower()
        if userResponse == 'yes' or userResponse == 'y':
            newItem()
        else:
            addItem = False

# Function to search for an item
def itemSearch():
    global inventory
    print('Please enter the item you are searching for: ', end='')
    userResponse = input().lower()
    if userResponse in inventory:
        print('Quantity: %(Quantity)s Price: %(Price)s Description: %(Description)s' % (inventory[userResponse]))
    else:
        print('Item not in inventory')

# Function to ask user if they want to search for an item
def askSearch():
    search = True
    while search is True:
        print('Would you like to search for an item in the inventory? ', end='')
        userResponse = input().lower()
        if userResponse == 'yes' or userResponse == 'y':
            itemSearch()
        else:
            search = False

# Initialize dictionary
inventory = {}

askUser()
askSearch()

print(inventory)