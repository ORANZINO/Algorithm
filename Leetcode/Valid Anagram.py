class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


'''
유효한 애너그램인지 판별하기 위해 두 문자열 모두 사전식으로 정렬 후 비교한다.
'''