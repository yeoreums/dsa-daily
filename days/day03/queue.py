queue = []

def enqueue(item):
    # TODO: add item to the queue
    queue.append(item)
    print(queue)

def dequeue():
    # TODO: remove and return the first item
    if queue:
        return queue.pop(0)
    return None

def run():
    enqueue("job1")
    enqueue("job2")
    enqueue("job3")

    print(dequeue())
    print(dequeue())

    print(queue)

if __name__ == "__main__":
    run()
