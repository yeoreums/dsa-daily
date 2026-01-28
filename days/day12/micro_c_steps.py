def walk_forward(start, steps):
    pos = start
    history = []

    for step in range(steps):
        # TODO:
        # move forward by 1
        # record (position, step_number)
        step_forward = step + 1
        pos += 1
        history.append((step_forward, pos))

    return history

def run():
    print(walk_forward(0, 3))
    # expected:
    # [(1, 1), (2, 2), (3, 3)]

if __name__ == "__main__":
    run()
