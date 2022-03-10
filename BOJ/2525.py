hour, minute = map(int, input().split())
time = int(input())
plus_hour, minute = (minute + time) // 60, (minute + time) % 60
print(f'{(hour + plus_hour) % 24} {minute}')

