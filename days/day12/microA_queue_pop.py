from collections import deque

def run():
    q = deque()

    # TODO:
    # add 3 numbers to the queue
    for i in range(3):
        q.append(i)
        # print(q)

    # TODO:
    # pop and print them one by one
    while q:
        print(q.popleft())

if __name__ == "__main__":
    run()
