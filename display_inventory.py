stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print 'Inventory:'
    items_total = 0
    for k, v in inventory.items():
        print inventory[k], k
        items_total += inventory[k]
    print "Total number of items:", items_total
    return items_total


print displayInventory(stuff)
