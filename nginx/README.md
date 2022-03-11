# Nginx

https://hub.docker.com/repository/docker/tot0ro/nginx-neo

```bash
$ docker run -d --name nginx \
 --network intra-net \                            # Web App(Django)와 DataBase(MariaDB)와 연결
 -v <THIS REPO>/nginx/conf.d:/etc/nginx/conf.d \  # Server config volume 연결
 -v <THIS REPO>/nginx/app:/usr/share/nginx/app \  # Server data volume 연결
 -p 80:8000 \
 tot0ro/nginx-neo
```

- 내부 포트 8000
- conf와 app 디렉토리를 마운트 해야함

### v0.1.0

nginx 서버 기본적으로 동작.

### v0.2.0 latest

wcgi를 통해 Django와 연동
