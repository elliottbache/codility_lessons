"""
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

content_copy
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)
content_copy

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

content_copy
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # count suffix sum for each element
    n = len(A)
    suffix_sum = [0] * n
    for i in range(n-2,-1,-1):
        suffix_sum[i] = suffix_sum[i+1] + A[i+1]

    # set passing_cars to 0
    passing_cars = 0

    # loop through A
    for i in range(n):

        # if element == 0, add suffix sum to passing_cars
        if A[i] == 0:
            passing_cars += suffix_sum[i]

    if passing_cars > 1000000000:
        return -1
    else:
        return passing_cars

if __name__ == "__main__":
    A = [0, 1,0, 1, 1]
    print(solution(A))