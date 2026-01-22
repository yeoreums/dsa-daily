def is_bad(version):
    # pretend this talks to a system
    return version >= 4

def first_bad_version(n):
    # versions are 1 to n
    # TODO: return the first bad version
    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2
        
        if is_bad(mid):
            right = mid
            print(mid)
        else:
            left = mid + 1
            print(mid)

    return left

def run():
    print(first_bad_version(7))  # expected: 4

if __name__ == "__main__":
    run()
