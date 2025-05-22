'''
Our hero Teemo is attacking an enemy Ashe with poison attacks!
When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds.
More formally, an attack at second t will mean Ashe is poisoned during
the inclusive time interval [t, t + duration - 1]. If Teemo attacks again
before the poison effect ends, the timer for it is reset, and the poison
effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries,
where timeSeries[i] denotes that Teemo attacks Ashe at second
timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.
'''
from typing import List


def find_poisoned_duration(time_series: List[int], duration: int) -> int:
    if not time_series:
        return 0

    total = 0
    for i in range(len(time_series) - 1):
        gap = time_series[i + 1] - time_series[i]
        total += min(gap, duration)

    # Add full duration for the last attack
    total += duration

    return total


print(find_poisoned_duration([1, 2, 3, 4, 5], 5))
