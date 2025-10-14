# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(X, Y, D):
    # Implement your solution here
    return math.ceil((Y-X)/D)

if __name__ == '__main__':

    print(solution(10, 85, 30))
    print(solution(10, 11, 30))