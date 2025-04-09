'''
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.
You must write an algorithm with O(log n) runtime complexity.
The main proble here is to make this algorithm logarithmic
we can achieve this by splitting the array in half, thus
shortening the problem everytime by 2
'''


def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid  # Target found
        if nums[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    # If target is not found, left will be the insertion position
    return left


print(search_insert([2], 2))  # output 0
print(search_insert([1, 3, 5, 6], 4))  # output 2
