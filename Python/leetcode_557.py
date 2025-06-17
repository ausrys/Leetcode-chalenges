def reverse_words(s: str) -> str:
    reversed_l = [x[::-1] for x in s.split()]
    return " ".join(reversed_l)


reverse_words("Let's take LeetCode contest")
