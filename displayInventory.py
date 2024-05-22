stuff = {'rope': 2, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    output = "Inventory:\n"
    total = 0
    for x in inventory:
        output += f"{inventory[x]} {x}\n"
        total += inventory[x]
    output += f"Total number of items: {total}"
    print(output)

displayInventory(stuff)
if __name__ == "__main__":
    displayInventory(stuff)
