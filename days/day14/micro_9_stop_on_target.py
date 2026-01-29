from collections import deque

def micro_stop_on_target():
    q = deque()
    q.append((0, 0))

    target = 2

    while q:
        value, step = q.popleft()
        print(value, step)

        # TODO:
        # if the current value is the target,
        # stop immediately and report the step
        if value == target:
            return step

        # TODO:
        # otherwise, if step is less than a limit (e.g. 3),
        # expand using the same +/- 1 rule
        max_step = 3
        if step < max_step:
            q.append((value - 1, step + 1))
            q.append((value + 1, step + 1))


def run():
    micro_stop_on_target()

if __name__ == "__main__":
    run()
