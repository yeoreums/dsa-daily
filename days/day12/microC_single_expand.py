from collections import deque

def run():
    q = deque()

    # TODO:
    # add (5, 0)
    q.append((5, 0))

    value, steps = q.popleft()

    # TODO:
    # add (value - 1, steps + 1)
    # add (value + 1, steps + 1)
    q.append((value - 1, steps + 1))
    q.append((value + 1, steps + 1))

    print(list(q))

if __name__ == "__main__":
    run()
