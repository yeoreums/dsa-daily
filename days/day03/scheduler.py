task_queue = []

def add_task(task):
    # TODO: add task to queue
    task_queue.append(task)
    print(task_queue)

def process_task():
    # TODO: process next task
    if task_queue:
        return task_queue.pop(0)
    return None

def run():
    add_task("email")
    add_task("backup")
    add_task("report")

    process_task()
    process_task()

    print(task_queue)

if __name__ == "__main__":
    run()
