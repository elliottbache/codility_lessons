# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here

    if not A:
        return A
    
    for j in range(K):

        last_element = A[-1]
        for i in range(len(A)):
            next_element = A[i]
            A[i] = last_element
            last_element = next_element

    return A



if __name__ == "__main__":
#    print(solution([3, 8, 9, 7, 6], 3))
    print(solution([], 3))