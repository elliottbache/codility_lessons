"""
This is a demo task.

Write a function:

def solution(A)
content_copy

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # convert to set to remove repeated elements
    B = set(A)

    # convert back to array to sort
    A = list(B)

    # sort array
    A.sort()
#    print(f"A = {A}")

    # find index of first positive element
    idx = 0
    while idx < len(A) and A[idx] <= 0:
        idx += 1
#    print(f"idx: {idx}")

    # slice to remove all <= 0
    if idx < len(A):
        B = A[idx:]
    # make sure we still have a non-empty A
    else:
        return 1
#    print(f"B = {B}")

    # loop through B
    for idx, x in enumerate(B):
        if x != idx + 1:
#            print(f"idx: {idx}, x: {x}")
            return idx + 1

    return len(B)+1

if __name__ == "__main__":
    print(solution([1, 3, 6, 4, 1, 2]))
    print(solution([1, 2, 3]))
    print(solution([-1, -3]))