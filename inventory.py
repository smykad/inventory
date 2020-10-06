# *******************************
# * Author: Doug Smyka          *
# * Application: Inventory      *
# * Date Created: 10.6.2020     *
# * Date Revised: 10.6.2020     *
# *******************************

def addNewItem(info):
    global inventory
    inventory[info[0]] = {'Quantity': info[1], 'Price': info[2], 'Description': info[3]}


inventory = {}

v1 = input()
v2 = input()
v3 = input()
v4 = input()

addNewItem([v1, v2, v3, v4 ])

print(inventory)