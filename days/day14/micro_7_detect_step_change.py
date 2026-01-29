from collections import deque

def micro_detect_step_change():
    q = deque()

    # queue with mixed steps
    q.append((0, 0))
    q.append((-1, 1))
    q.append((1, 1))
    q.append((-2, 2))
    q.append((0, 2))

    prev_step = None

    while q:
        value, step = q.popleft()

        # TODO:
        # if prev_step is None, just print step
        # if step != prev_step, print "step changed to X"
        # otherwise, just print step

        if prev_step is None:
            print(step)
        elif step != prev_step:
            print(f"Step changed to {step}")
        else:
            print(step)
        
        prev_step = step


def run():
    micro_detect_step_change()

if __name__ == "__main__":
    run()
