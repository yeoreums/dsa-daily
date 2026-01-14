counts = {}

def add_event(event):
    # TODO: count events
        counts[event] = counts.get(event, 0) + 1
        # print(counts)

def get_frequent_events(threshold):
    # TODO: return a new dict with only events >= threshold
    result = {}
    for key, value in counts.items():
        if value >= threshold:
            result[key] = value
    return result

def run():
    events = ["login", "login", "logout", "login", "logout", "logout"]

    for e in events:
        add_event(e)

    result = get_frequent_events(2)
    print(result)

if __name__ == "__main__":
    run()
