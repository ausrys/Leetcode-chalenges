'''
Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''


def search_range(nums, target):
    def find_left():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def find_right():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left_index = find_left()
    right_index = find_right()

    # Validate if target actually exists in range
    if left_index <= right_index:
        return [left_index, right_index]

    return [-1, -1]


print(search_range([5, 7, 7, 8, 8, 10], 7))
