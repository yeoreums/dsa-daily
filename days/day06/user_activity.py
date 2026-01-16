unique_users = set()
action_counts = {}

def process_event(event):
    # event is a tuple: (user_id, action)
    # TODO:
    # 1. record unique users
    # 2. count actions per user
    unique_users.add(event[0])
    action_counts[event[0]] = action_counts.get(event[0], 0) + 1

def run():
    events = [
        ("u1", "login"),
        ("u2", "login"),
        ("u1", "logout"),
        ("u1", "login"),
        ("u2", "login"),
    ]

    for e in events:
        process_event(e)

    print("Unique users:", unique_users)
    print("Action counts:", action_counts)

if __name__ == "__main__":
    run()
