# 실습 4C-1

from typing import Any
from collections import deque


class Stack:
    def __init__(self, maxlen: int = 256) -> None:
        """ 스택 초기화 """
        self.capacity = maxlen        # 스택의 크기
        self.__stk = deque([], maxlen=maxlen)    # 스택 본체

    def __len__(self) -> int:
        """ 스택에 쌓여있는 데이터 개수를 반환 """
        return len(self.__stk)

    def is_empty(self) -> bool:
        """스택이 비어있는지 판단"""
        return not self.__stk

    def is_full(self) -> bool:
        """스택이 가득찬지 판단"""
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        """스택에 value를 추가"""
        self.__stk.append(value)

    def pop(self) -> None:
        """스택에 데이터를 꺼냄"""
        return self.__stk.pop()

    def peek(self) -> Any:
        """ 꼭대기 데이터를 확인함 """
        return self.__stk[-1]

    def clear(self) -> None:
        """ 스택을 비움 """
        self.__stk.clear()

    def find(self, value: Any) -> int:
        """ 스택에서 value를 찾아 인덱스를 반환 """
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        """ 스택에있는 value 갯수를 반환 """
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        """ 스택에 value가 있는지 판단 """
        return self.count(value)

    def dump(self) -> None:
        """ 덤프 """
        print(list(self.__stk))