'''
You are given a large integer represented as an integer array
digits, where each digits[i] is the ith digit of the integer. The digits are
ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

We loop through the list from the last digit, then check if current
element is bigger smaller than 9, if not we change it to 0 and go
to the next iteration untill we can add 1. If we cant add 1 and
we reach the end, we put add two arrays, with 1 being in front.
'''


def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits


# Test cases
print(plus_one([1, 2, 3]))  # Output: [1, 2, 4]
print(plus_one([2, 9, 9]))         # Output: [3,, 0 0]
