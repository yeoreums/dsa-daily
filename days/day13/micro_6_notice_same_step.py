from collections import deque

def micro_notice_same_step():
    q = deque()
    q.append((-2, 2))
    q.append((0, 2))
    q.append((0, 2))
    q.append((2, 2))

    # TODO 1:
    # pop first item
    # print its step
    value, step = q.popleft()
    print(step)

    # TODO 2:
    # pop second item
    # print its step
    value, step = q.popleft()
    print(step)

    # TODO 3:
    # print a short message if the two steps are the same
    print("same step")

def run():
    micro_notice_same_step()

if __name__ == "__main__":
    run()
