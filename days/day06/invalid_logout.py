logged_in = set()
invalid_users = set()

def process_event(event):
    # event is (user_id, action)
    # TODO:
    # - login → add user to logged_in
    # - logout:
    #     - if user not in logged_in → mark invalid
    #     - else remove from logged_in
    user, action = event

    if action == "login":
        logged_in.add(user)
    elif action == "logout":
        if user not in logged_in:
            invalid_users.add(user)
        else:
            logged_in.remove(user)

def run():
    events = [
        ("u1", "login"),
        ("u2", "logout"),
        ("u1", "logout"),
        ("u3", "logout"),
        ("u2", "login"),
        ("u2", "logout"),
    ]

    for e in events:
        process_event(e)

    print(invalid_users)

if __name__ == "__main__":
    run()
