from typing import List
import heapq


def find_kth_largest(nums: List[int], k: int) -> int:
    heap: list[int] = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


print(find_kth_largest(nums=[2, 1, 1], k=2))
