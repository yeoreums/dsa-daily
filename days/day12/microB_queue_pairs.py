from collections import deque

def run():
    q = deque()

    # TODO:
    # add (10, 0)
    # add (11, 1)
    q.append((10, 0))
    q.append((11, 1))

    # TODO:
    # pop and print both
    while q:
        print(q.popleft())

if __name__ == "__main__":
    run()
