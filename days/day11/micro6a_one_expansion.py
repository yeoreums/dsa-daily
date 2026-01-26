from collections import deque

def run():
    q = deque()

    # TODO: add (2, 0)
    q.append((2, 0))

    floor, presses = q.popleft()

    # TODO:
    # add (floor - 1, presses + 1)
    # add (floor + 1, presses + 1)

    q.append((floor -1, presses + 1))
    q.append((floor + 1, presses + 1))

    print(list(q))

if __name__ == "__main__":
    run()
