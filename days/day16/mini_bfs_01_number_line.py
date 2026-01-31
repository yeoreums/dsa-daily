from collections import deque

def min_steps(start, target):
    # your code here
    q = deque()
    q.append((start, 0))

    visited = set()
    visited.add(start)

    while q:
        position, step = q.popleft()
        if position == target:
            return step
        
        for next_position in (position - 1, position + 1):
            if next_position not in visited:
                visited.add(next_position)
                q.append((next_position, step + 1))


def run():
    print(min_steps(0, 5))   # expected: 5
    print(min_steps(3, -2))  # expected: 5


if __name__ == "__main__":
    run()
