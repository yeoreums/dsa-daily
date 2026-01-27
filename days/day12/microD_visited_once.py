from collections import deque

def run():
    q = deque()
    visited = set()

    # TODO:
    # add (3, 0)
    # mark 3 visited
    q.append((3, 0))
    visited.add(3)

    value, steps = q.popleft()

    # TODO:
    # generate next values
    # only add unseen ones
    q.append((value - 1, steps + 1))
    q.append((value + 1, steps + 1))
    visited.add(value + 1)
    visited.add(value - 1)

    # Correct pattern:
    # if value - 1 not in visited:
    #     visited.add(value - 1)
    #     q.append((value - 1, steps + 1))



    print(list(q))
    print(visited)

if __name__ == "__main__":
    run()
