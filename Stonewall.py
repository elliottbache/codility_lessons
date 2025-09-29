"""
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

def solution(H)
content_copy

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:

  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8

content_copy
the function should return 7. The figure shows one possible arrangement of seven blocks.



Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array H is an integer within the range [1..1,000,000,000].
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # initialize counter and stack for holding last block
    counter = 1
    last_blocks = [H[0]]

    # loop through H
    for i in range(1,len(H)):

        # height of last block in stack
        last_block = measure_last_block(last_blocks)

        # if block larger than last in stack, add to counter and stack
        if H[i] > last_block:

            counter += 1
            last_blocks.append(H[i])

        # if block is smaller than last in stack, remove last in stack
        elif H[i] < last_block:

            # remove all blocks from stack that are too big
            while H[i] < last_block:

                last_blocks.pop()
                last_block = measure_last_block(last_blocks)

            # if block is not equal to last in stack, add to counter
            if H[i] != last_block:

                counter += 1
                last_blocks.append(H[i])

    return counter

def measure_last_block(last_blocks: list[int]) -> int:
    """
    Returns height of last block in stack
    :param last_blocks: stack of all remaining blocks
    :return: height of last block.  0 if stack is empty
    """
    if len(last_blocks) == 0:

        return 0

    else:

        return last_blocks[-1]

if __name__ == '__main__':
    assert solution([8, 8, 5, 7, 9, 8, 7,4, 8]) == 7
    assert solution([2, 5, 1, 4, 6, 7, 9, 10, 1]) == 8