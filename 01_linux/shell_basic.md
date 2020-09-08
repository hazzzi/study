# 1. Shell

## 1.1. 유닉스 쉘 소개

### 1.1.1. 리눅스 구조

- 커널
  - 프로그램 실행 : 메모리로 불러옴
  - 프로그램 종료 : 메모리에서 제거
- 쉘
  - 사용자와 커널의 의사소통 도구

### 기본 명령어
- [x] touch
- [x] cat
- [x] head
- [x] tail
- [x] grep
- [x] mv
- [x] rm
- [x] find
- [x] cp
- [x] cd
- [x] ls
- [x] pwd
- [x] mkdir

#### 쉘
- /etc/passwd

| \$USER |     |      |      |     | \$HOME    | \$SHELL   |
| :----- | :-- | :--- | :--- | :-- | :-------- | :-------- |
| app    | x   | 1003 | 1003 | ,,, | /home/app | /bin/bash |


- 명령행 분석
  1. 히스토리 기능을 사용하여 명령어를 치환
  2. 명령행이 토큰 단위로 분리
  3. 히스토리 내열을 갱신
  4. 인용 부호를 처리
  5. 친환할 별명이 있는지 검사, 함수 정의
  6. 리다이렉션화, 백그라운드, 파이프 설정
  7. 변수 치환(e.g. $user, $name 등)
  8. 명령어 치환(e.g. date)
  9. 글러빙이라는 파일 이름 치환(e.g. cat abc.??, rm *.c)
  10. 프로그램 수행

- 0: stdin
- 1: stdout
- 2: stderr
- 2> 에러를 리다이렉션함

- 파이프를 사용하면 출력을 다른 명령어의 입력으로 보낼 수있음

### 나중에 수정
lsb_release -a : os 버전 보는 명령어

|grep (명령어 찾아보기)

centos : httpd
ubuntu : apache2

sudo service wildfly restart (서비스 재시작 -> outofMemory)
tai