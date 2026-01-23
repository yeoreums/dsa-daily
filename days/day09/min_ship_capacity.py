def can_ship(weights, D, capacity):
    days = 1
    current = 0

    for w in weights:
        if current + w <= capacity:
            current += w
        else:
            days += 1
            current = w

    return days <= D


def min_ship_capacity(weights, D):
    # TODO: return the minimum capacity to ship within D days
    left = max(weights)
    right = sum(weights)
    
    while left < right:
        mid = (left + right) // 2
        if can_ship(weights, D, mid):
            right = mid
        else:
            left = mid + 1
    return left


def run():
    weights = [3, 2, 2, 4, 1, 4]
    D = 3
    print(min_ship_capacity(weights, D))  # expected: 6


if __name__ == "__main__":
    run()
