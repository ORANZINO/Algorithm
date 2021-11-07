while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break

"""
EOF를 처리하기 위해 Error handling을 포함.
Loop에서 a + b를 출력하는 문제
"""