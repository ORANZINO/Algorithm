def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for i, price in enumerate(prices):
        # stack이 비었으면 false
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
    return answer


"""
스택을 적절히 활용하면 풀 수 있는 문제.
순서대로 element를 확인하며 stack의 맨 위에 있는 수보다 더 작다면 그렇지 않을 때까지 pop하면 된다.
그리고 나서 해당 element의 index를 stack에 넣어준다.
pop할 때는 해당 시점에서 index만큼을 빼서 얼마나 가격이 떨어지지 않았는지 계산하면 된다.
"""