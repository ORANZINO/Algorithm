from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits

"""
isdigit() method를 활용하여 letter log와 digit log를 구분
lambda function을 이용한 sort 방식으로 letter log들을 정렬한다.
마지막에 digit이 모두 뒤에 가게 함으로써 리턴
"""