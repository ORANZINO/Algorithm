from typing import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
        return merged


'''
배열의 첫 번째 원소를 기준으로 정렬하면 순차적으로 
뒤에 있는 배열의 첫 번쨰  앞에 있는 배열의 범위에 속하는지 점검함으로써
병합할지 말지를 결정할 수 있다. loop을 도는 리스트 내에서 인덱스 변화가 있으면 안되므로
별도의 리스트를 생성하여 병합을 수행할 수 있도록 한다.
'''