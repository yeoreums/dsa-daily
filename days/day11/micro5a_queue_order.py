from collections import deque

def run():
    q = deque()

    # TODO: add (2, 0) 
    # TODO: add (3, 1)
    # TODO: take two item out and print it

    q.append((2, 0))
    q.append((3, 1))

    print(q.popleft())
    print(q.popleft())

if __name__ == "__main__":
    run()
