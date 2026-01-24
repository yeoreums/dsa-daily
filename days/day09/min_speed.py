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

        # If this speed works, we try to go *slower*
        # because we want the minimum speed that still works
        if can_finish(piles, H, mid):
            right = mid
        else:
            left = mid + 1

    # left == right
    # Smallest speed that still finishes within H hours
    return left

def run():
    piles = [3, 6, 7, 11]
    H = 8
    print(min_speed(piles, H))  # expected: 4


if __name__ == "__main__":
    run()

# piles totla = 27
# 3 * 8h = 24 can't finish it
# 4 * 8h = 32, can finish it 