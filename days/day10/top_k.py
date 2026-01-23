import heapq

def top_k(nums, k):
    heap = []

    for n in nums:
        # TODO:
        # 1) push n into heap
        # 2) if heap size > k, remove smallest
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap


def run():
    nums = [5, 1, 3, 10, 2]
    print(top_k(nums, 3))  # expected: 3 largest numbers

if __name__ == "__main__":
    run()
