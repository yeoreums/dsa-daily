user_actions = {}

def process_event(event):
    # event is a tuple: (user_id, action)
    # TODO:
    # store unique actions per user
    user, action = event
    
    if user not in user_actions:
        user_actions[user] = set()
    
    user_actions[user].add(action)
    

def run():
    events = [
        ("u1", "login"),
        ("u1", "login"),
        ("u1", "logout"),
        ("u2", "login"),
        ("u2", "login"),
        ("u2", "purchase"),
    ]

    for e in events:
        process_event(e)

    print(user_actions)

if __name__ == "__main__":
    run()
