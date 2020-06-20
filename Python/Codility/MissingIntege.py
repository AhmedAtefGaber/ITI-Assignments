def solution(A):
"""
Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer 
(greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.
"""   
    mx=max(A)
    if mx <= 0:
        return 1
    else:
        for i in range(1,mx):
           if i not in A:
               return i
        else:
            return mx+1 