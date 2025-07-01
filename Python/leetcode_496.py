from typing import List


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    result: List[int] = []
    for num in nums1:
        nums2_i = nums2.index(num)
        was_found = False
        for nums in nums2[nums2_i:]:
            if nums > num:
                result.append(nums)
                was_found = True
                break
        if was_found is False:
            result.append(-1)
    return result
