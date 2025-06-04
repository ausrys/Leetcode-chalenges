from typing import List


def find_relative_ranks(score: List[int]) -> List[str]:
    rank_list = ["Gold Medal", "Silver Medal", "Bronze Medal"]

    # Sort scores in descending order with original indices
    sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])

    result = [""] * len(score)

    for i, (idx, val) in enumerate(sorted_scores):
        if i < 3:
            result[idx] = rank_list[i]
        else:
            result[idx] = str(i + 1)

    return result


print(find_relative_ranks([1]))
