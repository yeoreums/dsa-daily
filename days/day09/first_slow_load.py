def is_slow(load):
    return load >= 6

def first_slow_load(n):
    # loads are from 1 to n
    # TODO: return the first slow load
    left = 1
    right = n
    
    while left < right:
        mid = (left + right) // 2
        if is_slow(mid):
            right = mid
        else:
            left = mid + 1
    return left

def run():
    print(first_slow_load(8))  # expected: 6

if __name__ == "__main__":
    run()
