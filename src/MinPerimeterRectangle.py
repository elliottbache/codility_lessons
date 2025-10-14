"""
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

def solution(N)
content_copy

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N: int) -> int:
    """Calculate the minimum perimeter of a rectangle given its area.

    The divisors (a) and their conjugates (N/a) are used to calculate
    perimeters.  The minimal perimeter is returned.  The sides are only
    integers.

    Args:
        N (int): the area of the rectangle.

    Returns:
        int: the minimal perimeter of the rectangle.
    """

    # set the initial minimal_perimeter as an impossibly high value
    i, minimal_perimeter = 1, 4*N
    while i ** 2 <= N:

        # if we find one divisor "a" then its conjugate "n/a" is also a
        # divisor
        if N % i == 0:
            if 2 * (N//i + i) < minimal_perimeter:
                minimal_perimeter = 2 * (N//i + i)

        i += 1

    return minimal_perimeter

if __name__ == '__main__':
    assert solution(30) == 22