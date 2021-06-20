import sys
input = sys.stdin.readline

t = int(input())
arr = [[10], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]

for _ in range(t):
    a, b = map(int, input().split())
    a %= 10
    b %= len(arr[a])
    print(arr[a][b - 1])

// 각 입력된 수에 따라 마지막 컴퓨터를 궁금해하므로 총 컴퓨터의 대수인 10으로 나누어준다.
// 각 수에서 몇 번째 원소에 해당하는지 
