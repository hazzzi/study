# 재귀 알고리즘

## 재귀(recursion)
- 재귀적 정의(recursive definition)
  - ex) 자연수의 정의 -> 1은 자연수, 어떤 자연수의 바로 다음 수도 자연수
- 재귀 호출(recursive call)
- 직접 재귀(direct): 함수 내부에서 자기 자신 호출
- 간접 재귀(indirect): 다른 함수를 통해 자신과 똑같은 함수 호출

### 팩토리얼
- 0! = 1
- n > 0 이면 n! = n * (n-1)!
  
### 유클리드 호제법
- 두 정수값의 최대 공약수(Greatest Common Divisor)
- x = az 와 y = bz를 만족하는 정수 a,b와 최대의 정수 z가 존재할때 z는 gcd(x,y)
    -> y가 0이면 x, y가 0이 아니면 gcd(y, x % y)
- example
  - 직사각형 안을 정사각형 여러개로 가득채워나갑니다. 이렇게 만들수있는 정사각형 가운데 가장 작은 정사각형이 변의 길이를 구하라.