def solution(msg):
    dic = {chr(ord('A') + i): i + 1 for i in range(26)}
    i, new = 0, 27
    answer = []
    while i < len(msg):
        k = 1
        while (i + k + 1) <= len(msg) and msg[i:i+k+1] in dic:
            k += 1
        if (i + k + 1) <= len(msg):
            dic[msg[i:i+k+1]] = new
            new += 1
            answer.append(dic[msg[i:i+k]])
        else:
            answer.append(dic[msg[i:i+k]])
        i += k
    return answer

