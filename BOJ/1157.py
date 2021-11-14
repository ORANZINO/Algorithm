from collections import Counter


counter = Counter(input().upper()).most_common()
if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print("?")
else:
    print(counter[0][0])


"""
Counter 라이브러리를 사용하여 가장 많이 나온 알파벳을 출력.
이 때, 대소문자를 통일하기 위해 upper() 함수를 사용했다. 
"""