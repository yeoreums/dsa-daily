WINDOW_SIZE = 5
window = []

def add(value):
    """
    Add a value to the window.
    If capacity is exceeded, remove the oldest item.
    """
    # TODO: implement
    if len(window) == WINDOW_SIZE:
        window.pop(0)
    window.append(value)


def run():
    for i in range(1, 11):
        add(i)
        print(window)


if __name__ == "__main__":
    run()
