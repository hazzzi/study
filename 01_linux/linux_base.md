## 4장 시작과 종료

#### 명령어

- 종료
  - poweroff,
  - shutdown -P now
  - halt -p
  - init 0
- 재부팅
  - shutdown -r now
  - reboot
  - init 6
- 로그아웃

  - exit
  - logout

- history : 썼던 명령어를 확인 할수있음.
- man 명령어 : 명령어 도움말 (스페이스 누르면 페이지 단위로 넘어감)
- umount 마운트 해제

#### vi

- x 하나 삭제
- yy 한줄 복사
- dd 한줄 삭제
- p 붙여넣기
- :set number 숫자 보이기

## 사용자의 권한

/etc/passwd :: 사용자 정보파일
/etc/group :: 그룹 정보파일
/etc/shadow :: 사용자 비밀번호파일 (암호화 되어있음)

### 사용자

root:x:0:0
사용자이름:암호:사용자ID:사용자가소속된그룹ID:추가정보:홈디렉터리:기본셸

### 그룹

ubuntu:x:1000:
그룹명:비밀번호:그룹id:보조 그룹 사용자

#### 명령어

adduser - 새로운사용자 추가 (--gid 로 그룹을 지정해줄수있음)
passwd - 사용자의 비밀번호 지정/변경
usermod - 사용자의 속성을 변경
userdel -사용자를 삭제 (사용자의 홈디렉터리는 안지워지지만 -r 옵션으로 지울수있음)
chage - 사용자의 암호를 주기적으로 변경하도록 설정

groups - 현재 사용자가 속한 그룹을 보여줌 (사용자는 무조건 하나이상의 그룹에 들어가있어야함)
groupadd - 새로운 그룹을 생성
groupmod -그룹의 속성을 변경
groupdel - 그룹을 삭제
gpasswd - 그룹 암호 설정(일반적으로 사용을 잘 하지는 않음)

#### 정보

새로운 사용자를 만들때 마다 /etc/skel/ 아래에있는 정보가 똑같이 생김

### 파일과 디렉터리 소유와 허가권

-rw-r--r-- 1 root root 0 7월 15 16:11 sample.txt
파일유형/파일 허가권/링크수/파일소유자이름/그룹이름/파일크기/마지막변경날짜, 시간/ 파일이름

파일 유형 : d 디렉터리 / - 일반파일
파일 허가권
rw- : 소유자
r-- : 그룹
r-- : 그외 사용자
(r :read, w: write, x: execute)

#### 명령어

chmod - 파일의 허가권 변경 (o:일반 사용자, g:그룹, u: 소유자)
ex) chmod 777 sample.txt
ex) chmod o-r sample.txt
ex) chmod u+w sample.txt

chown - 파일의 소유권 변경(chwon, chgrp), root 사용자만 쓸수있음
ex) chwon ubuntu.ubuntu sample.txt
chwon 사용자.그룹 sample.txt (파일의 소유권을 사용자.그룹으로 변경해라)

#### 링크

- 하드 링크 : inode블록을 같이 공유하는거, 하드링크파일만 하나 생성되며 같은 inode1을 공유함
- 심볼릭 링크 : 윈도우의 바로가기라고 생각하면된다, inode2를 가르키고 inode2가 원본파일포인터를 가르키고 원본파일포인터가 원본파일을 가르킨다(원본파일이 없으면 접 근을 못한다.)

###### 명령어

ln - 링크를 생성
ex) ln 링크대상파일이름 링크파일이름 (-s 옵션이 소프트링크 생성)

#### 프로그램 설치를 위한 dpkg

윈도우 setup.exe 와 비슷한 설치 파일
확장명 \*.deb이며 이를 패키지라고 부름
패키지이름 버전-개정번호 아키텍처.deb

###### 명렁어

- dpkg -i 패키지파일이름.deb : 설치
- dpkg -r 패키지이름 : 삭제
- dpkg -P 패키지이름 : 설정파일까지 삭제
- dpkg -l 패키지이름 : 설치된 패키지에 대한 정보를 보여줌
- dpkg -L 패키지이름 : 패키지가 설치한 파일 목록을 보여줌
- dpkg --info 패키지파일이름.deb :패키지 파일에 대한 정보를 보여줌

- 단점 : 의존성 문제가 있음
- 이를 해결하기 위해 apt-get이 등장함

#### apt-get

- dpkg 명령의 패키지 의존성 문제를 완전하게 해결됨
- 인터넷을 통하여 필요한 파일을 저장소에서 자동으로 모두 다운로드해서 설치하는 방식
- /etc/apt/source.list 파일에 패키지 목록이 있음

##### 명령어

- apt-get install 패키지 이름 : 기본 설치 (-y yes 옵션)
- apt-get update : 패키지 목록의 업데이트
- apt-get remove/purge 패키지 이름: 삭제
- apt-get autoremove : 사용하지 않는 패키지 제거
- apt-get clean / apt-get autoclean : 내려받은 파일 제거(자주안씀)
- apt-cache : 패키지 설치 전에 패키지에 대한 정보나 의존성문제를 미리 확인
- apt-cache show 패키지이름 : 패키지 정보보기
- apt-cache depends 패키지이름 : 패키지 의존성 확인
- apt-cache rdepends 패키지이름 : 패키지 역의존성 확인

###### 동작 과정

1. apt-get install 입력
2. /etc/apt/sources.list 파일을 열어서 url 주소확인
3. 설치와 관련된 패키지 목록을 요청(우분투 패키지 저장소에서)
4. 설치와 관련된 패키지 목록만 다운로드
5. 설치할패키지와 관련된 패키지의 이름을 화면에 출력
6. y를 입력하면 설치에 필요한 패키지 파일 요청함
7. 설치할 패키지 파일을 다운로드해서 자동 설치

###### 우분투 패키지 저장소

- main : 우분투에서 공식적으로 지원하는 무료 sw
- universe : 우분트에서 지원하지않는 무료 sw
- restricted : 우분투에서 공식적으로 지원하는 유료sw
- multiverse : 우분투에서 지원하지 않는 유료 sw
- /etc/apt/sources.list 파일에 기록되어잇음

### 파일 압축

파일 자체가 압축됨 기존파일이 남아있지는 않음
zip은 예외 / window랑 비슷하다고 생각하면댐

##### 명령어

- xz 파일이름(-d 압축해제)
- bzip2 파일이름(-d 압축해제)
- gzip 파일이름(-d 압축해제)
- zip 압축파일이름 압축할파일이름(unzip 파일이름 압축해제)
- tar : 파일 묶기의 명령어(압축과는 별개의 프로그램으로 수행)
  - 자주 쓰이는게 tar cvf / tar xvf
  - 동작 : c(묶기), x(풀기), t(경로확인)
  - 옵션 : f(파일), v(과정보이기), J(tar+xz), z(tar+gzip), j(tar+bzip)

### 파일 위치 검색

`find [경로] [옵션] [조건] [action]` : 기본 파일 찾기

- `[옵션]` -name, -user(소유자), -newer(전, 후), -perm(허가권), -size(크기)
- `[action]` -print(디폴트), -exec(외부명령 실행)
  ex) `# find /etc -name "*.conf"`
  ex) `# find /bin -size +10k -size -100k`
  ex) `# find /home -name "*.swp" -exec rm {} \;`
  `-exec` : 외부명령어의 시작 `\;` : 외부명령어의 끝

### cron 과 at

cron
주기적응로 반복되는 일을 자동적으로 실행될 수 있도록 설정

- /etc/crontab 에서 관리
- 분 시 일 월 요일 사용자 실행명령
  - ex) `00 05 1 \* \* root cp -r /home /backup`

at
일회성 작업을 예약

- 예약 : # at <시간>
  - ex) `at 3:00am tomorrow` 내일 새벽 3시
  - ex) `at now + 1 hours` 한시간 후
- at> 프롬프트에 예약명령어 입력 후 enter
- 완료되면 ctrl + d
- 확인 : at -I
- 취소 : atrm <작업번호>

#### NOTE

- 우분투는 총 7개의 모니터를 제공
  단축키는 ctrl + alt + f1~f6
  f7은 x윈도우모드임
- head -5 : 앞부분 5줄 보기
- tail -3 : 꼬리부분 3줄 보기

- init 명령어 뒤에 붙는 숫자는 런레벨이라고 부름 (0,1,3,5,6 번정도는 기억하랭) /lib/systemd/system 에 runlevel?.target 파일에서 확인할 수있다거함.
- default runlevel을 변경할 수 있음.
