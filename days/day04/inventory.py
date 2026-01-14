inventory = {}

def add_item(item):
    # TODO: increase count for this item
    inventory[item] = inventory.get(item, 0) + 1
    print(inventory)    # debugging & checking

def run():
    add_item("apple")
    add_item("banana")
    add_item("apple")
    add_item("orange")
    add_item("banana")
    add_item("apple")

    print(inventory)

if __name__ == "__main__":
    run()
