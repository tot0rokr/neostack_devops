# Neostack devops project

## Jenkins

https://hub.docker.com/repository/docker/tot0ro/jenkins-blueocean-neo

#### v0.1.0

Nordic nRF Mesh SDK를 컴파일 하기 위한 cmake compile 환경 세팅

## Nginx

https://hub.docker.com/repository/docker/tot0ro/nginx-neo

내부 포트 8000 

아래 디렉토리를 nginx conf와 html 디렉토리에 마운트 해야함

```
-v <THIS REPO>/nginx/conf.d:/etc/nginx/conf.d
-v <THIS REPO>/nginx/www:/usr/share/nginx/www
```

#### v0.1.0

nginx 서버 기본적으로 동작.

## Django
