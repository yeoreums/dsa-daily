undo_stack = []
redo_stack = []

def do(action):
    # TODO:
    # 1) push action to undo_stack
    # 2) clear redo_stack
    undo_stack.append(action)
    redo_stack.clear()

def undo():
    # TODO:
    # if undo_stack empty: return None
    # pop from undo_stack -> move to redo_stack -> return it
    if undo_stack:
        undo_item = undo_stack.pop()
        redo_stack.append(undo_item)
        return undo_item
    else:
        return None

def redo():
    # TODO:
    # if redo_stack empty: return None
    # pop from redo_stack -> move to undo_stack -> return it
    if redo_stack:
        redo_item = redo_stack.pop()
        undo_stack.append(redo_item)
        return redo_item
    else:
        return None



def run():
    do("type A")
    do("type B")
    do("save")

    print("undo:", undo())  # save
    print("undo:", undo())  # type B

    print("redo:", redo())  # type B
    print("redo:", redo())  # save

    do("rename file")       # this should clear redo history

    print("redo:", redo())  # None

    print("undo_stack:", undo_stack)
    print("redo_stack:", redo_stack)

if __name__ == "__main__":
    run()
