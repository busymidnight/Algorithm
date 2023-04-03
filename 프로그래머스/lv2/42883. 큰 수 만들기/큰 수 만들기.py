import itertools


def solution(number, k):
    print(list(map(''.join, itertools.combinations(number, k)))) # 2개의 원소로 수열 만들기
 