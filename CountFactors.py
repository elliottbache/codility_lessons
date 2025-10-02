"""
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)
content_copy

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    """Count the number of divisors of an integer N

    Count the number of divisors assuming that if a is a divisor of n,
    then n/a is also a divisor.  We only need to count up to sqrt(n)

    Args:
        N (int) : an integer

    Returns:
        int: the number of divisors of N
    """
    i, result = 1, 0
    while i**2 < N:

        # if we find one divisor "a" then its conjugate "n/a" is also a
        # divisor
        if N % i == 0:
            result += 2

        i += 1

    # if the sqrt of N is an integer, only add one more divisor (the sqrt)
    if i**2 == N:
        result += 1

    return result

if __name__ == '__main__':
    assert solution(24) == 8