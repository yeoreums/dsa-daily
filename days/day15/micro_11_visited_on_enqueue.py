from collections import deque

def micro_visited_on_enqueue():
    q = deque()
    q.append((0, 0))

    visited = set([0])  # starting value is already seen

    max_step = 3

    while q:
        value, step = q.popleft()
        print(value, step)

        # TODO:
        # if step is still below max_step:
        #   generate next possible values
        #   but only enqueue them if they have NOT been visited yet
        #   when you enqueue, mark them as visited immediately
        if step < max_step:
            n_value = value - 1
            if n_value not in visited:
                visited.add(n_value)
                q.append((n_value, step + 1))
            
            n_value = value + 1
            if n_value not in visited:
                visited.add(n_value)
                q.append((n_value, step + 1))

def run():
    micro_visited_on_enqueue()

if __name__ == "__main__":
    run()
