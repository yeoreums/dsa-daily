from collections import deque

queue = deque()

def enqueue(task):
    # TODO:
    # add task to the queue
    queue.append(task)
    # print(queue)

def dequeue():
    # TODO:
    # remove and return the oldest task
    # return None if empty
    if queue:
        item = queue.popleft()
        # print(item)
        return item
    else:
        return None

def run():
    enqueue("task-1")
    enqueue("task-2")
    enqueue("task-3")

    print(dequeue())  # task-1
    print(dequeue())  # task-2

    enqueue("task-4")

    print(dequeue())  # task-3
    print(dequeue())  # task-4
    print(dequeue())  # None

if __name__ == "__main__":
    run()
