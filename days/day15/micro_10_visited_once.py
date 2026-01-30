from collections import deque

def micro_visited_once():
    q = deque()
    q.append((0, 0))

    visited = set()

    max_step = 3

    while q:
        value, step = q.popleft()
        print(value, step)

        # TODO:
        # if this value has already been seen before,
        # skip expanding it
        if value in visited:
            continue
        else:
            visited.add(value)
        
        if step < max_step:
            q.append((value - 1, step + 1))
            q.append((value + 1, step + 1))

        # TODO:
        # otherwise:
        # - mark this value as visited
        # - if step is still below max_step,
        #   expand using the same +/- 1 rule

def run():
    micro_visited_once()

if __name__ == "__main__":
    run()
