def displayInventory(inventory):
    print 'Inventory:'
    items_total = 0
    for k, v in inventory.items():
        print inventory[k], k
        items_total += inventory[k]
    print "Total number of items:", items_total
    return items_total


def addInventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)
    return inventory

dragonloot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'rope': 1, 'gold coin': 42}


inv = addInventory(inv, dragonloot)
displayInventory(inv)
