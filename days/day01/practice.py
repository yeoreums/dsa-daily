items = []

def add(value):
    # TODO: add value to items
    items.append(value)


def run():
    for i in range(1, 6):
        add(i)
        print(items)


if __name__ == "__main__":
    run()
