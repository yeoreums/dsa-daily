def reachable_in_two(start):
    # TODO:
    # compute all floors reachable in exactly 2 moves
    one = {start - 1, start + 1}
    two = set()

    for i in one:
        two.add(i - 1)
        two.add(i + 1)        
        # print(two)

    return two

def run():
    print(reachable_in_two(2))  # expected: {0, 2, 4}

if __name__ == "__main__":
    run()
