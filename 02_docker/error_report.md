### 해결방안

###### cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is th docker daemon running?

도커 서비스가 실행이 안되어있는 상태

```linux
$ systemctl status docker 

도커 서비스 상태를 확인 하면 inactive 상태

$ systemctl start docker 

로 시작 시켜준다
```