from collections import deque

def micro_step_limit():
    q = deque()
    q.append((0, 0))

    max_step = 2

    while q:
        value, step = q.popleft()
        print(value, step)

        # TODO:
        # only expand this state if its step is less than max_step
        # expansion means appending the next possible states
        if step < max_step:
            q.append((value - 1, step + 1))
            q.append((value + 1, step + 1))

def run():
    micro_step_limit()

if __name__ == "__main__":
    run()
