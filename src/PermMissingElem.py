"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)
content_copy

that, given an array A, returns the value of the missing element.

For example, given array A such that:

A[0] = 2 A[1] = 3 A[2] = 1 A[3] = 5
content_copy
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Sort array
    A.sort()

    # Extreme cases
    if not A:
        return 1
    if A[-1] != len(A) + 1:
        return len(A) + 1

    for i in range(len(A)):
        if A[i] != i+1:
            return i+1

if __name__ == '__main__':
    print(solution([4, 2, 3, 5, 1, 6, 8, 9]))
    print(solution([2, 3, 1, 5]))
    print(solution([]))
    print(solution([1]))
    print(solution([2]))
    print(solution([2, 3, 1, 5, 4]))
    print(solution([2, 3, 4, 5]))
    print(solution([2, 3, 1, 1]))
    print(solution([1, 3]))
    print(solution([2, 3]))
    print(solution([1, 2]))
