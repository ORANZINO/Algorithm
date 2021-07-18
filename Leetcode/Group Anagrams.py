import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for s in strs:
            anagrams[''.join(sorted(s))].append(s)

        return anagrams.values()

"""
각 단어를 정렬함으로써 아나그램을 구분하였다.
알게된 점1: sorted()를 string에 바로 써도 리스트로 변환해서 정렬해준다.
알게된 점2: defaultdict를 사용하여 default 형태를 설정하는 것이 가능하다.
"""
