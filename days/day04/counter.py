counts = {}

def add_event(event):
    # TODO: increase count for this event
    if event in counts:
        counts[event] += 1
        print(counts)
    else:
        counts[event] = 1
        print(counts)

def run():
    add_event("login")
    add_event("login")
    add_event("logout")
    add_event("login")

    print(counts)

if __name__ == "__main__":
    run()
