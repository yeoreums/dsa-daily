undo_stack = []

def do(action):
    # TODO: record a new action
    undo_stack.append(action)

def undo():
    # TODO: undo the most recent action
    if undo_stack:
        undo_stack.pop()
    

def run():
    do("open file")
    do("write text")
    do("save file")

    undo()
    undo()

    print(undo_stack)

if __name__ == "__main__":
    run()
