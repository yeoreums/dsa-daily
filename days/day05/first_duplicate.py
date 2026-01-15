seen = set()

def find_first_duplicate(items):
    # TODO: return the first duplicate item
    for item in items:
        if item in seen:
            return item
        seen.add(item)

def run():
    items = ["apple", "banana", "apple", "orange"]
    dup = find_first_duplicate(items)
    print(dup)

if __name__ == "__main__":
    run()
