'''
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen
numbers is different.

The test cases are generated such that the number of unique
combinations that sum up to target is less than 150 combinations
for the given input.
'''


def combination_sum(candidates, target):
    result = []

    def backtrack(start, current_combination, total):
        if total == target:
            result.append(list(current_combination))
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])
            # allow reuse of same number
            backtrack(i, current_combination, total + candidates[i])
            current_combination.pop()  # backtrack

    backtrack(0, [], 0)
    return result
