# 실습 2-2
# 시퀀스 원소의 최댓값 출력하기
# Sequence >> list, bytearry, str, tuple, bytes
# 모듈 >> 하나의 스크립트 프로그램
from typing import Any, Sequence


def max_of(a: Sequence) -> Any:  # 파라미터 a는 Sequence형, return 값은 Any
    """ 시퀀스형 a 원소의 최댓값을 반환 """
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


if __name__ == '__main__':
    num = int(input('원소의 수를 입력하세요'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요:'))

    print(f'최댓값은 {max_of(x)}입니다.')
