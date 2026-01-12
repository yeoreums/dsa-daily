items = []

def add(value):
    # TODO:
    # add value only if it is not already in items
    if value not in items:
        items.append(value)


def run():
    for i in [1, 2, 2, 3, 1, 4]:
        add(i)
        print(items)


if __name__ == "__main__":
    run()
