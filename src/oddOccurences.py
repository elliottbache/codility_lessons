import timeit
import random

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
"""
def solution(A):
    # loop through array while len > 1
    len_a = len(A)
    while len_a > 1:
        # pop last element and find index of its occurrence
        last_element = A.pop()
        len_a -= 1

        # if no occurrence, then return
        if last_element in A:
            A.remove(last_element)
            len_a -= 1
        else:
            return last_element
        
    if A:
        return A[0]
    else:
        return []
"""
"""
def solution(A):
    # loop through array while len > 1
    len_a = len(A)
    while len_a > 1:
        # pop last element and find index of its occurrence
        last_element = A.pop()
#        print("last_elemetn = ",last_element)

        for idx, item in enumerate(A):

            if item == last_element:
                del A[idx]
#                print("A = ",A)
                break


        


        # if no occurrence, then return
        if last_element in A:
            A.remove(last_element)
        else:
            return last_element
        
    if A:
        return A[0]
    else:
        return []
"""
def solution(A):
    odd = set()
    for v in A:
        if v in odd:
            odd.remove(v)
        else:
            odd.add(v)
    # If you expect exactly one unpaired element:
    if len(odd) == 1:
        return next(iter(odd))
    
if __name__ == "__main__":
    A = random.sample(range(1, 1000000000), 100003)
    print(min(timeit.repeat(
    lambda: solution(A),
    number=1
)))
    print(solution([9, 3, 9, 3, 9, 7, 9]))
    print(solution([42]))
