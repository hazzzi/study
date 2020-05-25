# 1. Python Basic

## 1.1. 문자열과 바이트
### 1.1.1. str
- 파이썬의 문자열은 기본적으로 유니코드
- immutable 타입
- `r'문자열'` : Raw String을 직접사용(ex. 파일 경로)

#### 1.1.1.1. method
- partition()
  - 앞부분, 분리자, 뒷부분으로 값을 리턴함
  - ```python
      departure, _, arrival = "Seattle-Seoul".partition('-')
      print(departure)
      # 출력 : Seattle
    ```
- encode("UTF-8") / decode("UTF-8") 
  - 인코딩 / 디코딩 가능
### 1.1.2. format
| conversion | 의미                           |
| :--------- | :----------------------------- |
| %s         | 문자열(str()을 사용)           |
| %r         | 문자열(repr()을 사용)          |
| %c         | 문자(char)                     |
| %d         | 정수(int)                      |
| %f         | 부동소수(float)                |
| %e         | 지수형 부동소수(소문자/대문자) |
| %g         | 일반형(소문자/대문자)          |
| %o         | 8진수(소문자/대문자)           |
| %x         | 16진수(소문자/대문자)          |
| %%         | % 퍼센트 리터럴                |

## 1.2. 조건문 / 반복문
### 1.2.1. 조건문
- ```python
    # 기본 표현
    if 조건문:
      실행문장

    # 한줄 표현
    if 조건문 : 실행문  

    # if elif else 표현
    if 조건문:
      실행문
    elif 조건문:
      실행문
    else:
      실행문

    # pass : 특정 블럭/문장을 수행하지 않고 skip
    if 조건문:
      pass
     else:
      실행문
  ```
  
### 1.2.2. 반복문
- ``` python
    # while
    while 조건문:
      실행문

    # for : foreach 처럼 쓰임
    # 참고 :  range(stop) / range(start, stop) / range(start,stop,step)
    for i in range(11):
      실행문

    for s in list1:
      실행문  
  ```
## 1.3. 컬렉션
### 1.3.1. 리스트
- 동적 배열 / mutable
- `list[index]` : index는 음수를 사용할수있음(ex. -2: 뒤에서 2번째 요소)
- `list[startIndex : endIndex]` : index는 생략가능
- `list.append` : 추가
- `list = 11` : 변경
- `del list[index]` :삭제
- `list1 + list2` : 병합
- `list1 * 숫자` : 반복
- `list.index(요소)` : 검색
- `list.count(요소)` : 특정 요소의 갯수
- `list = [표현식 for 요소 in 컬렉션 [if 조건식]]` : 조건에 맞는 리스트 생성

---
# 2. NOTE
## 2.1. jupyter notebook short cut

### 2.1.1. 셀 선택 모드
| 단축키    | 내용                         |
| :-------- | :--------------------------- |
| a         | 위에 셀 추가                 |
| b         | 아래에 셀 추가               |
| dd        | 셀 삭제                      |
| x         | 잘라내기                     |
| c         | 복사                         |
| p         | 붙여넣기                     |
| shift + m | 아래 셀과 합치기             |
| m         | 셀 타입 변경 (마크다운)      |
| y         | 셀 타입 변경 (코드))         |
| ctrl+s, s | 셀 타입 변경 (파일 저장))    |
| [enter]   | 셀 타입 변경 (코드편집 모드) |

### 2.1.2. 코드 입력 모드
| 단축키           | 내용                      |
| :--------------- | :------------------------ |
| ctrl + enter     | 셀 실행                   |
| shift + enter    | 실행 후 다음셀 이동       |
| ctrl + z         | 실행 취소                 |
| ctrl + y         | 셀 다시 실행              |
| shift + ctrl + - | 커서에서 셀 나누기        |
| esc, ctrl + m    | 셀 타입 변경(셀선택 모드) |
| ctrl + /         | 주석 처리                 |
