def count_moves(start, target):
    # TODO:
    # starting from start, keep increasing by 1
    # count how many steps it takes to reach target
    count = 0
    while start < target:
        start += 1
        count +=1
    return count


def run():
    print(count_moves(2, 5))  # expected: 3

if __name__ == "__main__":
    run()
