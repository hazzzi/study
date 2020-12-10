# 실습 2-6
# 뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence


def reverse_array(a: MutableSequence) -> None:
    """ 뮤터블 시퀀스를 a의 원소를 역순으로 정렬 """
    n = len(a)
    for i in range(n // 2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == '__main__':
    nx = int(input('원소 수:'))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요'))

    reverse_array(x)

    for i in range(nx):
        print(f'x[{i}] = {x[i]}')