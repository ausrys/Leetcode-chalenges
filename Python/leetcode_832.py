'''
Given an n x n binary matrix image, flip the image horizontally,
then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is
reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1
is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
'''

from typing import List


def flip_and_invert_image(image: List[List[int]]) -> List[List[int]]:
    replacements = {1: 0, 0: 1}
    replace = replacements.get
    for arr in image:
        arr[:] = arr[::-1]
        arr[:] = [replace(n, n) for n in arr]
    return image


print(flip_and_invert_image(
    [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
