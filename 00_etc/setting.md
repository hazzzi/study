# Chocolaty

choco install -y jdk8 -params 'installdir=c:\\java\\8'
choco install -y googlechrome
choco install -y notepadplusplus
choco install -y vscode
choco install -y git
choco install -y telegram
choco install -y d2codingfont
choco install -y honeyview
choco install -y bandizipz

choco install -y nodejs
choco install -y yarn

choco install -y dbeaver
choco install -y postman

# IntelliJ
Jetbrains Intellij IDEA 2018.3.6 and webstorm 2018.3.6 version crack
https://blog.naver.com/adonise007/221501262591

# SSH Key 생성
생성방법  : ssh-keygen -t rsa
생성위치  : ~/.ssh
공개키확인:  cat id_rsa.pub

# gitlab clone
http://jjfive.net:18080

http://jjfive.net:18080/profile/keys

./clone-*.sh

#파일서버 위치
\\192.168.114.5



#### content type 나중에 정리
POST /html/daq.html
Content-Type: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36

{"result":{"success":true},"data":{"mobiList":[{"mobiId":1000005,"mobiType":"이륜","chassis":"KR90R1Z3EKZX7F796","displayCarNumber":" ","lat":37.12345,"lng":126.849,"battery":50,"state":"DRIVING"}]}}


POST /html/daq.html
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36

userName=james&age=13
===
POST /html/daq.html
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36

userName=james&Jane&age=13
userName=james%26Jane&age=13


===
GET /html/daq.html?userName=홍길동
Content-Type: x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36

===
GET /html/daq.html?userName=홍길동
Content-Type: text/html
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36

====
파일 업로드 
POST /html/daq.html
Content-Type: multipart/form-data

===============
fieldName=userName 
james
===============
fieldName=age
13
==fjaskdfjasdjfa===========
fieldName=myfile;fileName=c:\바탕화면\거래내역.txt
fas===============jkldfaklsdfkasdjf;asjkl;dfja;skldfjal;sdjkfkl;asdfjkl;asd 
fasjkldfjasdf asdflasdf
===============



POST /html/daq.html
Content-Type: graphql

{
   User {
      age 
	  name
   }
}





