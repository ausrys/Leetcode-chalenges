def add_strings(num1: str, num2: str) -> str:
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
        digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0

        total = digit1 + digit2 + carry
        result.append(str(total % 10))
        carry = total // 10

        i -= 1
        j -= 1

    return ''.join(reversed(result))
