# 실습 4-3
# 고정길이 큐 클래스 구현

from typing import Any


class FixedQueue:
    class Empty(Exception):
        """큐가 비어있을 때"""
        pass

    class Full(Exception):
        """큐가 가득차있을 때"""
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0                     # 현재 데이터 갯수
        self.front = 0                  # 맨 앞 원소의 커서
        self.rear = 0                   # 맨 끝 원소의 커서
        self.capacity = capacity        # 큐의 크기
        self.que = [None] * capacity    # 큐

    def __len__(self) -> int:
        """큐에있는 모든 데이터의 갯수"""
        return self.no

    def is_empty(self) -> bool:
        """ 큐가 비어있는지 여부 """
        return self.no <= 0

    def is_full(self) -> bool:
        """ 큐가 가득 차있는지 여부"""
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        """데이터를 인큐"""
        if self.is_full():
            raise FixedQueue.Full

        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
        print(f'front: {self.front}', end='')

    def deque(self) -> Any:
        """데이터를 디큐"""
        if self.is_empty():
            raise FixedQueue.Empty

        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        """ 데이터를 peek """
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        """큐에서 value를 찾아 인덱스 반환"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value: Any) -> int:
        """큐에있는 value의 갯수를 반환"""
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        """큐에 value가 있는지 판단"""
        return self.count(value)

    def clear(self) -> None:
        """큐의 모든 데이터를 비움"""
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        """모든 데이터를 순서대로 출력"""
        if self.is_empty():
            raise FixedQueue.Empty
        else:
            for i in range(self.no):
                print(self.que[(i+self.front) % self.capacity], end='')
            print()
