def solution(A, B):
    n = len(A)
    A.sort()
    B.sort()
    answer = i = j = 0
    while i < n and j < n:
        if B[j] > A[i]:
            i += 1
            answer += 1
        j += 1

    return answer