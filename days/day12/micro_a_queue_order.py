from collections import deque

def serve_people(arrivals):
    q = deque()
    order = []

    # TODO:
    # 1. add all arrivals to the queue
    # 2. serve them one by one
    # 3. return the serving order
    for j in arrivals:
        q.append(j)

    for i in q:
        order.append(i)
    # Better one for BFS later:
    # while q:
    #   order.append(q.popleft())
    return order

def run():
    print(serve_people(["A", "B", "C"]))
    # expected: ["A", "B", "C"]

if __name__ == "__main__":
    run()
