from collections import deque

def micro_expand_once():
    q = deque()

    # starting state: value 0 at step 0
    q.append((0, 0))

    # TODO 1:
    # pop one item from the queue
    # store it in value, step
    value, step = q.popleft()
    
    # TODO 2:
    # create two new states:
    #   value - 1 at step + 1
    #   value + 1 at step + 1
    # and append them to the queue
    q.append((value - 1, step + 1))
    q.append((value + 1, step + 1))

    # TODO 3:
    # print the queue
    print(q)

def run():
    micro_expand_once()

if __name__ == "__main__":
    run()
