"""
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbors. More
precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P]
and A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2

content_copy
has exactly three peaks: 3, 5, 10.

We want to divide this array into blocks containing the same number of
elements. More precisely, we want to choose a number K that will yield
the following blocks:

A[0], A[1], ..., A[K − 1],
A[K], A[K + 1], ..., A[2K − 1],
...
A[N − K], A[N − K + 1], ..., A[N − 1].
What's more, every block should contain at least one peak. Notice that
extreme elements of the blocks (for example A[K − 1] or A[K]) can also
be peaks, but only if they have both neighbors (including one in an
adjacent blocks).

The goal is to find the maximum number of blocks into which the array
A can be divided.

Array A can be divided into blocks as follows:

one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains
three peaks.
two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block
has a peak.
three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has
a peak. Notice in particular that the first block (1, 2, 3, 4) has a
peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the
adjacent block.
However, array A cannot be divided into four blocks, (1, 2, 3),
(4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks
do not contain a peak. Notice in particular that the (4, 3, 4) block
contains two peaks: A[3] and A[5].

The maximum number of blocks that array A can be divided into is three.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the
 maximum number of blocks into which A can be divided.

If A cannot be divided into some number of blocks, the function should
 return 0.

For example, given:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2

content_copy
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range
[0..1,000,000,000].
"""


def peaks_solution(A: list[int]) -> int:
    """Find the maximum number of equal blocks the array A can be
    divided into.

    The blocks should have an equal number of elements.  The peaks can
    be located on the edges of a block.

    Args:
        A (list[int]): An array of integers.

    Returns:
        int: The maximum number of blocks into which the array A can be
         divided.

    Examples:
        >>> A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
        >>> peaks_solution(A)
        3
    """

    # calculate possible integers that divide the mountain into
    # equal blocks
    divisors = integer_divisors(len(A))
    divisors.sort(reverse=True)

    # first element corresponds to 1-element blocks, which don't have
    # peaks
    divisors.pop(0)

    i = 0
    while i < len(divisors):

        n_divisors = divisors[i]
        n_elements = len(A)//n_divisors

        is_peak = False
        for j in range(n_divisors):

            # define limits for this block
            first_element = j*n_elements
            last_element = (j+1)*n_elements - 1

            # create list for this block plus the previous and next elements
            B = list()
            if j != 0:
                B.append(A[first_element-1])
            B.extend(A[first_element:last_element+1])
            if j != n_divisors - 1:
                B.append(A[last_element+1])

            # find first peak
            is_peak = False
            k = 1
            while k < len(B) - 1:
                if B[k] > B[k - 1] and B[k] > B[k + 1]:
                    is_peak = True
                    break
                k += 1

            # if no peak, break
            if not is_peak:
                break

        if is_peak:
            return n_divisors

        i += 1

    return 0


def integer_divisors(N: int) -> list[int]:
    """Count the number of divisors of an integer N

    Count the number of divisors assuming that if a is a divisor of n,
    then n/a is also a divisor.  We only need to count up to sqrt(n)

    Args:
        N (int) : an integer

    Returns:
        list[int]: the divisors of N

    Examples:
        >>> sorted(integer_divisors(12))
        [1, 2, 3, 4, 6, 12]
    """

    i = 1
    result = list()
    while i**2 < N:

        # if we find one divisor "a" then its conjugate "n/a" is also a
        # divisor
        if N % i == 0:
            result.append(i)
            result.append(N//i)

        i += 1

    # if the sqrt of N is an integer, only add one more divisor (the sqrt)
    if i**2 == N:
        result.append(i)

    return result


if __name__ == '__main__':
    A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
    print(peaks_solution(A))
