undo_stack = []

def do(action):
    # TODO:
    # record a new action
    undo_stack.append(action)

def undo():
    # TODO:
    # undo the most recent action
    # return the undone action, or None if empty
    if undo_stack:
        return undo_stack.pop()
    else:
        return None

def run():
    do("type A")
    do("type B")
    do("save")

    print(undo())  # expected: "save"
    print(undo())  # expected: "type B"
    print(undo())  # expected: "type A"
    print(undo())  # expected: None

if __name__ == "__main__":
    run()
