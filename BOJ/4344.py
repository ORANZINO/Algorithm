c = int(input())
for _ in range(c):
    arr = list(map(int, input().split()))[1:]
    avg = sum(arr) / len(arr)
    print(f'{round(sum(1 for a in arr if a > avg) / len(arr) * 100, 3):.3f}%')

'''
주어진 숫자들 중 평균을 넘지 못하는 숫자의 비율을 계산한다.
이 때, 소숫점 셋째자리까지 빈틈없이 출력돼야하므로 string formatting을 사용하도록 한다. 
'''