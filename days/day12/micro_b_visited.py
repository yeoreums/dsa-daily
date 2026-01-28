def unique_process(nums):
    visited = set()
    result = []

    for n in nums:
        # TODO:
        # if n not visited:
        #   mark visited
        #   process (append to result)
        if n not in visited:
            visited.add(n)
            result.append(n)

    return result

def run():
    print(unique_process([1, 2, 1, 3, 2, 4]))
    # expected: [1, 2, 3, 4]

if __name__ == "__main__":
    run()
