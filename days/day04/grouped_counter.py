counts = {}

def add_event(event):
    # event is a tuple: (type, status)
    # TODO: count by event type only
    counts[event[0]] = counts.get(event[0], 0) + 1

def run():
    events = [
        ("login", "success"),
        ("login", "fail"),
        ("login", "success"),
        ("logout", "success"),
        ("login", "success"),
    ]

    for e in events:
        add_event(e)

    print(counts)

if __name__ == "__main__":
    run()
