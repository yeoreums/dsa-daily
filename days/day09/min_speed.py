import math

def can_finish(piles, H, speed):
    hours = 0
    for p in piles:
        hours += math.ceil(p / speed)
    return hours <= H


def min_speed(piles, H):
    # TODO: return the minimum speed
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2
        if can_finish(piles, H, mid):
            right = mid
        else:
            left = mid + 1
    return left

def run():
    piles = [3, 6, 7, 11]
    H = 8
    print(min_speed(piles, H))  # expected: 4


if __name__ == "__main__":
    run()
