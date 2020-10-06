# *******************************
# * Author: Doug Smyka          *
# * Application: Inventory      *
# * Date Created: 10.6.2020     *
# * Date Revised: 10.6.2020     *
# *******************************


def addNewItem(info):
    global inventory
    inventory[info[0]] = {'Quantity': info[1], 'Price': info[2], 'Description': info[3]}


def newItem():
    print('item: ', end='')
    v1 = input()
    print('Quantity: ', end='')
    v2 = input()
    print('Price: ', end='')
    v3 = input()
    print('Description: ', end='')
    v4 = input()
    addNewItem([v1, v2, v3, v4 ])


def askUser():
    addItem = True
    while addItem is True:
        print('Would you like to add an item? ', end='')
        userResponse = input()
        if userResponse == 'yes' or userResponse == 'y':
            newItem()
        else:
            addItem = False


inventory = {}

askUser()

print(inventory)