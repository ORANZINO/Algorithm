from collections import Counter


def solution(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]

"""
Counter를 사용해서 풀 수 있는 문제.
Counter 객체끼리 빼면 각 key의 value들이 빠진다.
항상 완주하지 못한 선수는 한 명이므로 뺀 결과에서 남아있는 key가 정답이 된다.
"""