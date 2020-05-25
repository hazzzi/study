## 탐색
- pwd 
  - print work directory, 작업중인 디렉터리를 보여줌
- ls 
  - list segments 
- cd 
  - 디렉터리로 이동
- mkdir 
  - make directory
- rmdir 
  - remove directory
- mount 
  - 기존 파일시스템으로 sd카드나 usb를 마운트
- df
  - 파일 시스템의 디스크 공간에 대한 필수 정보를 표시

## 시스템 조작
- service
  - 시스템 전체 서비스를 호출하기 위한 명령어
  ```linux
    $ sudo service wildfly restart (서비스 재시작 -> outofMemory)
  ```
- shutdown
- batch
- kill
- ps
- uname    
## 파일 관리
- | grep 
  - 패턴 검색할때 사용, 정규식 터미널 명령
- find
  - 터미널에서 파일을 검색할때 사용
- cp
  - file/dir copy path1 -> path2
- mv
  - file/dir move path1 -> path2 
- cat
  - 파일의 내용을 볼수있음
- touch
  - qlsvkdlf todtjd  

## 기타
- lsb_release -a 
  - os 버전 보는 명령어
- echo
- sort
  - 정렬
- sudo
  - root 권한으로 사용
- chmod
  - change mode 
- chown
  - change owner
- clear
  - 콘솔창 클리어
- locate
  - 파일의 위치
- wget
  - 웹에서 파일을 다운로드 할때

centos : httpd
ubuntu : apache2

## jq
[jq 정리](https://github.com/cp949/study-linux/blob/master/README.jq.md)
```
$ docker inspect c-was-s0101 | jq '.[0] | .Mounts'
```

## bashrc
스크립트 명령어 추가할수있음
```linux
$ cat ~/.bashrc
```
