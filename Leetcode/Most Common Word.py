import collections
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        return collections.Counter(words).most_common(1)[0][0]

"""
정규표현식을 사용해서 전처리한 다음 Counter 라이브러리를 사용해 가장 빈도가 높은 단어를 출력한다.
알게된 점: 정규식 패턴에서 r은 raw string을 의미하며, 백슬래시(\)를 2번 쓰지 않기 위해서 사용한다.
"""