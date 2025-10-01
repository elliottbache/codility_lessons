"""
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

content_copy
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)
content_copy

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2

content_copy
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""
def solution(A: list[int]) -> int:
    """Compute the maximum double-slice sum in linear time.

    A double slice is defined by indices (X, Y, Z) with 0 <= X < Y < Z < N
    and sum(A[X+1:Y]) + sum(A[Y+1:Z]). The elements at X, Y, Z are excluded.

    Parameters
    ----------
    A : list[int]
        Input list of integers. Length N >= 3 is required to form
        a double slice.

    Returns
    -------
    int
        Maximum double-slice sum (0 if no positive sum exists).

    Notes
    -----
    We compute:
    - left[i]: max subarray sum ending just before i (over A[..i-1]),
      clipped at 0.
    - right[i]: max subarray sum starting just after i (over A[i+1..]),
      clipped at 0.

    The best double slice that excludes index i is left[i] + right[i].
    We take max over i in [1..N-2].
    """
    n = len(A)
    if n < 3:
        return 0

    left = [0] * n   # left[i] = max sum ending at i-1, >= 0
    for i in range(2, n - 1):
        left[i] = max(0, left[i - 1] + A[i - 1])

    right = [0] * n  # right[i] = max sum starting at i+1, >= 0
    for i in range(n - 3, 0, -1):
        right[i] = max(0, right[i + 1] + A[i + 1])

    best = 0
    for i in range(1, n - 1):
        best = max(best, left[i] + right[i])

    return best

if __name__ == '__main__':
    assert solution([3, 2, 6, -1, 4, 5, -1, 2]) == 17
    assert solution([5, 17, 0, 3]) == 17