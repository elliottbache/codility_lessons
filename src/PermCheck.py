"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

A[0] = 4 A[1] = 1 A[2] = 3 A[3] = 2
content_copy
is a permutation, but array A such that:

A[0] = 4 A[1] = 1 A[2] = 3
content_copy
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)
content_copy

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

A[0] = 4 A[1] = 1 A[2] = 3 A[3] = 2
content_copy
the function should return 1.

Given array A such that:

A[0] = 4 A[1] = 1 A[2] = 3
content_copy
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Convert to set
    B = set(A)

    # If duplicates then return 0
    if len(B) != len(A):
        return 0

    # Sort array
    A.sort()

    # Check if last element is equal to  the size
    if A[-1] == len(A):
        return 1
    else:
        return 0


if __name__ == "__main__":
    A = [4, 1, 3, 2]
    print(solution(A))
    A = [9, 5, 7, 3, 2, 7, 3, 1, 10, 8]
    print(solution(A))
    A = [1, 1]
    print(solution(A))
