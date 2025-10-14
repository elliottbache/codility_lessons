"""
Write a function:

def solution(A, B, K)
content_copy

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    import math

    n_divisible = math.floor(B/K) - math.floor(A/K)

    if A % K == 0:
        n_divisible += 1

    return n_divisible

if __name__ == "__main__":

    assert solution(4, 4, 3) == 0
    assert solution(4, 5, 3) == 0
    assert solution(4, 6, 3) == 1
    assert solution(4, 7, 3) == 1
    assert solution(5, 5, 3) == 0
    assert solution(5, 6, 3) == 1
    assert solution(5, 7, 3) == 1
    assert solution(5, 8, 3) == 1
    assert solution(6, 6, 3) == 1
    assert solution(6, 7, 3) == 1
    assert solution(6, 8, 3) == 1
    assert solution(6, 9, 3) == 2
    assert solution(6, 11, 2) == 3
    assert solution(0,14,2) == 8
    assert solution(11,345,17) == 20
    assert solution(0,0,11) == 1
