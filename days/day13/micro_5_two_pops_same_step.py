from collections import deque

def micro_two_pops_same_step():
    q = deque()

    # starting states: both at step 1
    q.append((-1, 1))
    q.append((1, 1))

    # TODO 1:
    # pop first item
    # expand it (value - 1, step + 1) and (value + 1, step + 1)
    value, step = q.popleft()
    q.append((value - 1, step + 1))
    q.append((value + 1, step + 1))

    # TODO 2:
    # pop second item
    # expand it the same way
    value, step = q.popleft()
    q.append((value - 1, step + 1))
    q.append((value + 1, step + 1))

    # TODO 3:
    # print the queue
    print(q)

def run():
    micro_two_pops_same_step()

if __name__ == "__main__":
    run()
