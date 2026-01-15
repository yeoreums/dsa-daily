seen = set()

def add_item(item):
    # TODO: store item only once
    seen.add(item)

def run():
    items = ["apple", "banana", "apple", "orange", "banana"]

    for i in items:
        add_item(i)

    print(seen)

if __name__ == "__main__":
    run()
