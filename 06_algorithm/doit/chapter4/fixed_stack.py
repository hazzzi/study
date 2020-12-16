
# 실습 4-1
# 고정 길이 스택 클래스 구현

from typing import Any


class FixedStack:

    class Empty(Exception):
        """ 비어있는 fixedStack에 pop 또는 peek할때 내보내는 예외처리 """
        pass

    class Full(Exception):
        """ 스택이 가득차면 내보내는 예외처리 """
        pass

    def __init__(self, capacity: int = 256) -> None:
        """ 스택 초기화 """
        self.stk = [None] * capacity    # 스택 본체
        self.capacity = capacity        # 스택의 크기
        self.ptr = 0                    # 스택 포인터

    def __len__(self) -> int:
        """ 스택에 쌓여있는 데이터 개수를 반환 """
        return self.ptr

    def is_empty(self) -> bool:
        """스택이 비어있는지 판단"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """스택이 가득찬지 판단"""
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        """스택에 value를 추가"""
        if self.is_full():
            return FixedStack.Full  # 스택이 가득찬 경우 예외 발생
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> None:
        """스택에 데이터를 꺼냄"""
        if self.is_empty():
            return FixedStack.Empty  # 스택이 비어있는 경우 예외 발생
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        """ 꼭대기 데이터를 확인함 """
        if self.is_empty():
            return FixedStack.Empty  # 스택이 비어있는 경우 예외 발생
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        """ 스택을 비움 """
        self.ptr = 0

    def find(self, value: Any) -> int:
        """ 스택에서 value를 찾아 인덱스를 반환 """
        for i in range(self.ptr - 1, -1, -1):  # 꼭대기 쪽부터 선형 검색
            if self.stk[i] == value:
                return i    # 검색 성공
        return -1           # 검색 실패

    def count(self, value: Any) -> int:
        """ 스택에있는 value 갯수를 반환 """
        c = 0
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        """ 스택에 value가 있는지 판단 """
        return self.count(value)

    def dump(self) -> None:
        """ 덤프 """
        if self.is_empty():
            print("스택이 비어있습니다")
        else:
            print(self.stk[:self.ptr])
