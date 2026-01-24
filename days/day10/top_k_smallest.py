import heapq

def top_k_smallest(nums, k):
    heap = []

    for n in nums:
        heapq.heappush(heap, -n)
        if len(heap) > k:
            heapq.heappop(heap)

    return [-x for x in heap]


def run():
    nums = [5, 1, 3, 10, 2]
    print(top_k_smallest(nums, 3))  # expected: 3 smallest numbers

if __name__ == "__main__":
    run()


# Using heapq to get smallest numbers instaed of biggest
# By turn into negative values and turn back in to positive