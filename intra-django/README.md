# Django

https://hub.docker.com/repository/docker/tot0ro/django-neo

```bash
$ docker run -d --name intra \
 --network intra-net \                   # DataBase(MariaDB)와 Server(Nginx)와 연결
 -v <THIS REPO>/intra-django/app:/app \  # Django Code volume 연결
 -e DJANGO_SECRET_KEY=<SECRET_KEY> \
 -e DB_NAME=<DB_NAME> \
 -e DB_USER=<DB_USER> \
 -e DB_PASS=<DB_PASS> \
 tot0ro/django-neo
```

- Nginx 보다 먼저 동작하여야 함.
- NginX 및 MariaDB와 같은 네트워크에 소속되어야 함
- SECRET\_KEY: django key이다. [여기서](https://miniwebtool.com/django-secret-key-generator/) 새 key를 생성할 수 있다.
- DB\_NAME: DB 이름. 해당 사이트에서 사용할 DB 이름이다.
- DB\_USER: 유저 계정 id. DB\_NAME을 사용할 권한이 있어야 한다.
- DB\_PASS: DB\_USER의 password.


### intra-v0.1.0

django 프로젝트 생성


### intra-v0.2.0

wcgi를 통해 nginx와 연동. nginx-neo v0.2.0과 호환

### intra-v0.3.0 latest

MariaDB와 연동. 사용할 db 및 user가 생성되어 있어야 함

- DB: intradb
- USER: intradb\_user
- PASS: intradb\_user
