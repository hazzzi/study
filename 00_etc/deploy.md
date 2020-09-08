
WAS = Web Application Server
오라클에서 J2EE 서버 스펙을 정의해놨고,,,,(스펙 = 인터페이스)
(ex: Tomcat, Wildfly(구 JBOSS)
유료 WAS: 웹스피어, JEUS(한국), WebLogic)

WAS에 메인함수 ==> 특정 패턴의 URL이 요청이 들어오면, 특정 서블릿을 실행해줘
/flawing/**/* ==> flawing.war , AAServlet의 service()메소드를 호출해줘
UserServlet, AdminServlet,UserListServlet

스프링이란? 서블릿을 한개로 통합했어
DispatcherServlet => Front Servlet

flawing.war 파일을 WAS에 배포하는 행위를 deploy라고 한다.

WAS에 설정한 특정 폴더에 war 파일을 가져다 놓으면 WAS가 그 war를 로드해준다.
그 폴더는 예를 들면 아래와 같다.
/home/app/wildfly/applications/instance1/deployments

일단은 임시폴더에 업로드하고, 임시폴더에서 deployments폴더에 복사하는 방식으로 deploy한다.

여기에 각종 스크립트
/home/app/wildfly/applications/script/instance1


app@192.168.114.28 // new1234!../

# 디플로이 과정 (로그 켜두고 확인)
1. war파일을 만든다.
2. 임시폴더에 업로드 (/home/app/NAS/wars/flawing)
3. 임시폴더에서 deployments폴더로 war파일 복사
cp flawing.war /home/app/wildfly/applications/instance1/deployments

보다 편리한 방법:
local => ./_build_dev.sh (war 파일 생성 및 서버의 임시폴더 업로드)
$  cd /home/app/wildfly/applications/script/instance1
$  ./deploy_flawing.sh

./mvnw cleanls => 메이븐 클린
scp => secure copy
- tail -f /home/app/wildfly/logs/s0101/server.log => WAS 로그파일
- tail -n 1000 /home/app/wildfly/logs/s0101/server.log => 뒤에서 1000줄 보기


~/flawing/mobi-simulator/run1.sh

scp build/libs/flawing-server-0.0.1-SNAPSHOT.war app@192.168.114.28:/home/app/NAS/wars/flawing/flawing.war


