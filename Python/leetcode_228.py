'''
ou are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers
in the array exactly. That is, each element of nums is covered by exactly
one of the ranges, and there is no integer x such that x is in one of the
ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''

from typing import List


def summary_ranges(nums: List[int]) -> List[str]:
    if not nums:
        return []

    ranges = []
    start = nums[0]

    for i in range(1, len(nums)):
        # If current number is not consecutive
        if nums[i] != nums[i - 1] + 1:
            end = nums[i - 1]
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{end}")
            start = nums[i]  # Start a new range

    # Handle the last range
    if start == nums[-1]:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}->{nums[-1]}")

    return ranges


print(summary_ranges([0, 2, 3, 4, 6, 8, 9]))
