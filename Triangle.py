"""
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

content_copy
Triplet (0, 2, 4) is triangular.

Write a function:

def solution(A)
content_copy

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

content_copy
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1

content_copy
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # sort A
    A.sort()

    # reverse A
    A.reverse()
#    print(f'A = {A}')

    # loop through A to check each element starting with largest to see if sum of following elements is greater
    for i in range(len(A) - 2):
        # check if A[-3] + A[-2] > A[-1]
#        print(f"A[-3] + A[-2] > A[-1] = {A[-3] + A[-2] > A[-1]}")
        if A[i+2] + A[i+1] > A[i]:
            return 1

    return 0

if __name__ == "__main__":
    assert solution([10, 2, 5, 1, 8, 20]) == 1
    assert solution([10, 50, 5, 1]) == 0