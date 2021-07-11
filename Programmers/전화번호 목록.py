def solution(phone_book):
    phone_book.sort()
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return True

"""
전화번호 목록을 sort하여 접두사가 항상 왼쪽으로 오게 한다.
zip()을 사용하여 모든 쌍이 검사받을 수 있도록 한다.
startswith()를 사용하여 접두사 검사
"""