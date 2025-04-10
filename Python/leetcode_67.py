'''
Given two binary strings a and b, return their sum as a binary string.
'''


def add_binary(a: str, b: str) -> str:
    result = []
    carry = 0

    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Iterate through the strings from the last digit to the first
    for i in range(max_len - 1, -1, -1):
        # Add corresponding bits and the carry from the previous step
        total = int(a[i]) + int(b[i]) + carry

        # Append the result bit (total % 2)
        result.append(str(total % 2))

        # Update the carry (total // 2)
        carry = total // 2

    # If there's a carry left, append it
    if carry:
        result.append('1')

    # Reverse the result and return as a string
    return ''.join(result[::-1])


# Example usage

print(add_binary("1111", "1111"))  # Ouput 11110
