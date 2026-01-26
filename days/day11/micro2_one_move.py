def reachable_in_one(start):
    # TODO:
    # return all floors reachable in exactly 1 move
    floors = set()
    floors.add(start + 1)
    floors.add(start - 1)
    return floors


def run():
    print(reachable_in_one(2))  # expected: [1, 3]

if __name__ == "__main__":
    run()
